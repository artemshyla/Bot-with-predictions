import torch
from torch import nn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from moexalgo import Ticker
from datetime import datetime, timedelta



class TestModel1(nn.Module):
    def __init__(self, input_size=1, hidden_size=128, output_size=1, num_layers=2, dropout=0.1):
        super().__init__()

        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.num_layers = num_layers
        self.dropout = dropout

        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True, num_layers=num_layers, dropout=dropout)
        self.linear = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.linear(x[:, -1, :])
        return x



def load_model(model_name: str):
    model_path = f'models/model_{model_name}.pt'
    checkpoint = torch.load(model_path, map_location='cpu')

    config = checkpoint['model_config']

    model = TestModel1(
        input_size=config['input_size'],
        hidden_size=config['hidden_size'],
        output_size=config['output_size'],
        num_layers=config['num_layers'],
        dropout=config['dropout']
    )

    model.load_state_dict(checkpoint['state_dict'])
    model.eval()
    return model



def create_predictions(model_name: str, days_for_preds: int):
    
    model = load_model(model_name)

    ticker = Ticker(model_name)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    data = pd.DataFrame(
        ticker.candles(start=start_date, end=end_date, period='1d')
        )

    closes = data[['close', 'begin']][-61:-1]
    dates = data['begin'][-2:-1]


    for _ in range(days_for_preds):
        


    return closes

print(create_predictions('SBER', 30))