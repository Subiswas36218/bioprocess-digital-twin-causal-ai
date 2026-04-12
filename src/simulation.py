import numpy as np
import pandas as pd

def generate_data(n=200):
    np.random.seed(42)

    time = np.arange(n)
    temperature = 37 + np.random.normal(0, 0.5, n)
    ph = 7 + np.random.normal(0, 0.2, n)
    nutrients = np.maximum(100 - time * 0.3 + np.random.normal(0, 2, n), 0)

    biomass = (
        0.5 * nutrients +
        2 * temperature -
        3 * abs(ph - 7) +
        np.random.normal(0, 5, n)
    )

    product = 0.8 * biomass + np.random.normal(0, 10, n)

    df = pd.DataFrame({
        "time": time,
        "temperature": temperature,
        "ph": ph,
        "nutrients": nutrients,
        "biomass": biomass,
        "product": product
    })

    return df


if __name__ == "__main__":
    df = generate_data()
    df.to_csv("data/simulated_data.csv", index=False)
    print("Data saved!")