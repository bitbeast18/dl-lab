from torch.utils.data import DataLoader
from .shared.datasets import HAPTDataset, RawHAPTDataset, hapt_collate
from .models.cnn_lstm import CNN_LSTM

def fetch_loaders():
    opt = {
        'batch_size': 32,
        'collate_fn': hapt_collate
    }

    psd_ds = DataLoader(HAPTDataset(), **opt)
    raw_ds = DataLoader(RawHAPTDataset(), **opt)

    return psd_ds, raw_ds

def fetch_model():
    return CNN_LSTM()

def train_epoch(loader, model, optim, criterion):
    for inp, true in loader:
        pred = model(inp)
        loss = criterion(true, pred)

        loss.zero_grad()
        loss.backward()
        optim.step()


def train(loader, model, optim):
    model.train()

    for epoch in epochs:
        loader = fetch_loader()

if __name__ == '__main__':
    model = fetch_model()
    psd_ldr, raw_ldr = fetch_loaders()

    train(psd_ldr, model, optim)
