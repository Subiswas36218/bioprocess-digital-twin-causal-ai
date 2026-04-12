import pandas as pd
import torch
from sklearn.preprocessing import StandardScaler
from model import BioprocessModel

def train():
    df = pd.read_csv("data/simulated_data.csv")

    X = df[["temperature", "ph", "nutrients", "biomass"]].values
    y = df["product"].values.reshape(-1, 1)

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.float32)

    model = BioprocessModel()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    loss_fn = torch.nn.MSELoss()

    for epoch in range(100):
        optimizer.zero_grad()
        preds = model(X_tensor)
        loss = loss_fn(preds, y_tensor)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Loss {loss.item()}")

    torch.save(model.state_dict(), "model.pth")
    print("Model saved!")

if __name__ == "__main__":
    train()