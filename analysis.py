from utils import arguments, theme, finish, plt, np
def demand(price,base_price,base_volume,elasticity):
    if min(price,base_price,base_volume)<=0: raise ValueError("Prices and volume must be positive")
    return base_volume*(price/base_price)**elasticity
def main():
    args=arguments(); theme()
    prices=np.linspace(70,150,161); base_price=100; base_volume=1000; cost=45; fixed=20000
    elasticities=[-1.,-1.5,-2.,-3.]
    fig,axes=plt.subplots(1,2,figsize=(12,4.5)); scenarios=[]
    for e in elasticities:
        volume=np.array([demand(p,base_price,base_volume,e) for p in prices])
        profit=(prices-cost)*volume-fixed; best=int(np.argmax(profit))
        assert np.all(np.diff(volume)<0)
        scenarios.append({"elasticity":e,"best_price_within_grid":prices[best],"profit_at_grid_best":profit[best],
          "volume_at_grid_best":volume[best],"boundary_optimum":bool(best in (0,len(prices)-1))})
        line,=axes[0].plot(prices,profit/1000,label=f"Elasticity {e:g}")
        boundary=best in (0,len(prices)-1)
        axes[0].scatter(prices[best],profit[best]/1000,facecolors="none" if boundary else line.get_color(),edgecolors=line.get_color(),s=55,zorder=3)
    metrics={"data_type":"ASSUMPTION-DRIVEN SIMULATION","base_price":base_price,"base_units":base_volume,
      "unit_variable_cost":cost,"fixed_cost":fixed,"baseline_profit":(base_price-cost)*base_volume-fixed,
      "price_grid_min":prices.min(),"price_grid_max":prices.max(),"scenarios":scenarios}
    assert np.isclose(demand(100,100,1000,-2),1000)
    axes[0].axvline(base_price,color="#94a3b8",linestyle="--",label="Baseline price")
    axes[0].axhline(0,color="#cbd5e1",linewidth=.8)
    axes[0].set(title="Profit sensitivity to price and elasticity",xlabel="Price (currency units)",ylabel="Profit (thousand currency units)")
    axes[0].legend(fontsize=8)
    for item in scenarios:
        boundary=item["boundary_optimum"]
        axes[1].scatter(item["elasticity"],item["best_price_within_grid"],facecolors="none" if boundary else "#087f8c",edgecolors="#087f8c",s=70)
        if boundary: axes[1].annotate("grid boundary",(item["elasticity"],item["best_price_within_grid"]),xytext=(5,5),textcoords="offset points",fontsize=8,color="#c96a4b")
    axes[1].axhline(base_price,color="#94a3b8",linestyle="--",label="Baseline price")
    axes[1].set(title="Grid-best price is assumption-sensitive",xlabel="Assumed price elasticity",ylabel="Best price within 70–150 grid",xticks=elasticities)
    axes[1].legend(fontsize=8)
    finish(args.output_dir,"Pricing Scenario Lab",metrics,
      ["The preferred grid price changes with elasticity; this illustrates model risk, not a discovered market optimum.",
       f"Baseline scenario profit is {metrics['baseline_profit']:,.0f} currency units per period.",
       "Validate demand response through research or controlled tests before turning scenarios into price decisions."],
      ["All inputs are invented assumptions. There is no empirical elasticity estimate.",
       "Price search is limited to 70–150; a boundary solution is not an unconstrained optimum.",
       "No competitor reactions, capacity limits, customer heterogeneity or price fairness constraints."],fig)
if __name__=="__main__": main()
