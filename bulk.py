import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import Tk

def read_asc_file(file_path):
    # Assuming the .asc file has two columns: Raman Shift and Intensity
    data = pd.read_csv(file_path, sep='\t', header=None, names=['Shift', 'Intensity'])
    return data

def stack_data(files):
    # Initialize an empty DataFrame to hold stacked data
    stacked_data = pd.DataFrame()
    for file in files:
        data = read_asc_file(file)
        if stacked_data.empty:
            stacked_data = data.set_index('Shift')
        else:
            # Align and average the intensities
            stacked_data = stacked_data.join(data.set_index('Shift'), how='outer', lsuffix='_left', rsuffix='_right')
            stacked_data['Intensity'] = stacked_data.mean(axis=1)
            stacked_data.drop(columns=[col for col in stacked_data.columns if 'Intensity_' in col], inplace=True)
    return stacked_data.reset_index()

def save_stacked_data(stacked_data, output_dir, subfolder_name):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{subfolder_name}_stacked.asc')
    stacked_data.to_csv(output_file, sep='\t', index=False, header=False)
    return output_file

def plot_data(stacked_data, output_dir, subfolder_name):
    plt.figure()
    plt.plot(stacked_data['Shift'], stacked_data['Intensity'])
    plt.xlabel('Raman Shift')
    plt.ylabel('Intensity')
    plt.title(f'Stacked Data for {subfolder_name}')
    output_file = os.path.join(output_dir, f'{subfolder_name}_chart.png')
    plt.savefig(output_file)
    plt.close()
    return output_file

# Main process
def process_folder():
    root = Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory()  # Prompt the user to select a directory
    new_folder_path = os.path.join(folder_path, 'processed')

    for subfolder_name in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder_name)
        if os.path.isdir(subfolder_path):
            # Find all .asc files in the subdirectory
            asc_files = [os.path.join(subfolder_path, f) for f in os.listdir(subfolder_path) if f.endswith('.asc')]
            if asc_files:
                # Stack the data from .asc files in the subfolder
                stacked_data = stack_data(asc_files)
                # Save the stacked data as a new .asc file
                save_stacked_data(stacked_data, new_folder_path, subfolder_name)
                # Plot and save the chart image
                plot_data(stacked_data, new_folder_path, subfolder_name)

if __name__ == '__main__':
    process_folder()
