# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:08:38 2020

@author: TrickyFox
"""

import numpy as np
import AnalizeTool
from scipy import special as sp

def sigmoid(x):
    return sp.expit(x)

def diff_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))

def make_synaptic_weights(x,n):
    return 2*np.random.random((x,n)) - 1

piece_factor = 5000
path_to_folder = "D:\\Программирование\\SPECPythonFedora\\SPEC_Pyhon_v2\\"
filenames = ["Ar рафит","Mn_24_04_20","W_1"]
ext = ".csv"
path_to_files = []

for s in filenames:
    path_to_files.append(path_to_folder+s+ext)
    
    
    
    
def Train(path_to_files, Iterations, piece_factor):
    
    PlotDatas = []
    PlotDatasIn = []

    for s in path_to_files:
        PlotData = AnalizeTool.csv_open(s)[1]
        PlotDatas.append(PlotData)
        PlotDatasIn += PlotData[1]

    FonByAlgs = []

    for i in PlotDatas:
        FonByAlg = AnalizeTool.AnalizeFon(i, 20, 5e-3, 5, 1 + 1e-2)[1]
        FonByAlgs += FonByAlg

    training_inputs = []
    training_outputs = []
    normalizers = []

    for it in range(len(PlotDatasIn)//piece_factor):
        normalizers.append(np.max(PlotDatasIn[it*piece_factor:(it+1)*piece_factor]))
        training_inputs.append(PlotDatasIn[it*piece_factor:(it+1)*piece_factor]/np.max(PlotDatasIn[it*piece_factor:(it+1)*piece_factor]))
        training_outputs.append(FonByAlgs[it*piece_factor:(it+1)*piece_factor]/np.max(PlotDatasIn[it*piece_factor:(it+1)*piece_factor]))

    temp = []
    for its in range((it+2)*piece_factor-len(PlotDatasIn)):
        temp.append(0)
        
    normalizers.append(np.max(PlotDatasIn[(it+1)*piece_factor:len(PlotDatasIn)]))
    training_inputs.append((PlotDatasIn[(it+1)*piece_factor:len(PlotDatasIn)]+temp)/np.max(PlotDatasIn[(it+1)*piece_factor:len(PlotDatasIn)]))
    training_outputs.append((FonByAlgs[(it+1)*piece_factor:len(FonByAlgs)]+temp)/np.max(PlotDatasIn[(it+1)*piece_factor:len(PlotDatasIn)]))
    
    training_inputs = np.array(training_inputs)
    
    first_layer_synapse_number = 150
    second_layer_synapse_number = 150

    first_layer_weights_matrix = make_synaptic_weights(piece_factor, first_layer_synapse_number)
    second_layer_weights_matrix = make_synaptic_weights(first_layer_synapse_number, second_layer_synapse_number)
    third_layer_weights_matrix = make_synaptic_weights(second_layer_synapse_number, piece_factor)
    
    for i in range(Iterations):
        first_layer_input = training_inputs
        first_layer_output = sigmoid(np.dot(first_layer_input, first_layer_weights_matrix))
        second_layer_input = first_layer_output
        second_layer_output = sigmoid(np.dot(second_layer_input, second_layer_weights_matrix))
        third_layer_input = second_layer_output
        output = sigmoid(np.dot(third_layer_input, third_layer_weights_matrix))

        third_layer_error = training_outputs - output
        third_layer_delta = third_layer_error*diff_sigmoid(output)
        
        second_layer_error = third_layer_delta.dot(third_layer_weights_matrix.T)
        second_layer_delta = second_layer_error*diff_sigmoid(second_layer_output)

        first_layer_error = second_layer_delta.dot(second_layer_weights_matrix.T)
        first_layer_delta = first_layer_error*diff_sigmoid(first_layer_output)

        third_layer_weights_matrix += third_layer_input.T.dot(third_layer_delta)
        second_layer_weights_matrix += second_layer_input.T.dot(second_layer_delta)
        first_layer_weights_matrix += first_layer_input.T.dot(first_layer_delta)
        
        print(i)
        
    np.save("l1_weights.npy",first_layer_weights_matrix)
    np.save("l2_weights.npy",second_layer_weights_matrix)
    np.save("l3_weights.npy",third_layer_weights_matrix)
    
def Calculate(path_to_file, piece_factor):
    
    PlotDatas = []
    PlotDatasIn = []
    PlotData = AnalizeTool.csv_open(path_to_file)[1]
    PlotDatas.append(PlotData)
    PlotDatasIn += PlotData[1]
    
    inputs = []
    normalizers = []
    it = -1
    for it in range(len(PlotDatasIn)//piece_factor):
        normalizers.append(np.max(PlotDatasIn[it*piece_factor:(it+1)*piece_factor]))
        inputs.append(PlotDatasIn[it*piece_factor:(it+1)*piece_factor]/np.max(PlotDatasIn[it*piece_factor:(it+1)*piece_factor]))
    temp = []
    for its in range((it+2)*piece_factor-len(PlotDatasIn)):
        temp.append(0)    
    normalizers.append(np.max(PlotDatasIn[(it+1)*piece_factor:len(PlotDatasIn)]))
    inputs.append((PlotDatasIn[(it+1)*piece_factor:len(PlotDatasIn)]+temp)/np.max(PlotDatasIn[(it+1)*piece_factor:len(PlotDatasIn)]))
    
    first_layer_weights_matrix = np.array([])
    second_layer_weights_matrix = np.array([])
    third_layer_weights_matrix = np.array([])
    
    first_layer_weights_matrix = np.load("l1_weights.npy")
    second_layer_weights_matrix = np.load("l2_weights.npy")
    third_layer_weights_matrix = np.load("l3_weights.npy")
    
    first_layer_input = inputs
    first_layer_output = sigmoid(np.dot(first_layer_input, first_layer_weights_matrix))
    second_layer_input = first_layer_output
    second_layer_output = sigmoid(np.dot(second_layer_input, second_layer_weights_matrix))
    third_layer_input = second_layer_output
    output = sigmoid(np.dot(third_layer_input, third_layer_weights_matrix))
    
    outputs = []
    inputs_denorm = []
    
    for i in range(len(output)):
        inputs_denorm.append(inputs[i]*normalizers[i])
        outputs.append(output[i]*normalizers[i])
    
    return inputs_denorm, outputs


Train(path_to_files, 10000, piece_factor)

path_to_file = "D:\\Программирование\\SPECPythonFedora\\SPEC_Pyhon_v2\\W_1.csv"
inputs, outputs = Calculate(path_to_file, piece_factor)

NeuronInput = []
NeuronOutput = []

NeuronInput.append(list(np.arange(0,len(inputs)*piece_factor,1)))
temp = []
for i in inputs:
    temp += list(i)
NeuronInput.append(temp)
NeuronOutput.append(list(np.arange(0,len(inputs)*piece_factor,1)))
temp = []
for i in outputs:
    temp += list(i)
NeuronOutput.append(temp)
print(NeuronOutput)

Path = "D:\\Программирование\\SPECPythonFedora\\SPEC_Pyhon_v2\\Neuron_Input.csv"
AnalizeTool.csv_save(Path, NeuronInput)
Path = "D:\\Программирование\\SPECPythonFedora\\SPEC_Pyhon_v2\\Neuron_Output.csv"
AnalizeTool.csv_save(Path, NeuronOutput)
