import pandas as pd
from dowhy import CausalModel

def causal_analysis():
    df = pd.read_csv("data/simulated_data.csv")

    graph = """
    digraph {
        nutrients -> biomass;
        temperature -> biomass;
        ph -> biomass;
        biomass -> product;
        temperature -> product;
    }
    """

    model = CausalModel(
        data=df,
        treatment="temperature",
        outcome="product",
        graph=graph
    )

    identified = model.identify_effect()
    estimate = model.estimate_effect(
        identified,
        method_name="backdoor.linear_regression"
    )

    print("Causal Effect of Temperature on Product:", estimate.value)

if __name__ == "__main__":
    causal_analysis()