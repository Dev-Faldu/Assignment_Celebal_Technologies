def analyze_target_distribution(df):
    """Analyze SalePrice distribution and apply transformations"""
    
    # Remove missing SalePrice (test set)
    train_data = df[df['SalePrice'].notna()].copy()
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # Original distribution
    axes[0,0].hist(train_data['SalePrice'], bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0,0].set_title('Original SalePrice Distribution', fontweight='bold')
    axes[0,0].set_xlabel('Sale Price ($)')
    axes[0,0].set_ylabel('Frequency')
    
    # Log-transformed distribution
    log_price = np.log1p(train_data['SalePrice'])
    axes[0,1].hist(log_price, bins=50, alpha=0.7, color='lightcoral', edgecolor='black')
    axes[0,1].set_title('Log-Transformed SalePrice Distribution', fontweight='bold')
    axes[0,1].set_xlabel('Log(Sale Price + 1)')
    axes[0,1].set_ylabel('Frequency')
    
    # Q-Q plot for normality assessment
    stats.probplot(log_price, dist="norm", plot=axes[0,2])
    axes[0,2].set_title('Q-Q Plot: Log-Transformed SalePrice', fontweight='bold')
    
    # Box plot by neighborhood (top 10)
    top_neighborhoods = train_data['Neighborhood'].value_counts().head(10).index
    subset_data = train_data[train_data['Neighborhood'].isin(top_neighborhoods)]
    
    axes[1,0].boxplot([subset_data[subset_data['Neighborhood'] == nbh]['SalePrice'] 
                      for nbh in top_neighborhoods], labels=top_neighborhoods)
    axes[1,0].set_title('SalePrice by Top 10 Neighborhoods', fontweight='bold')
    axes[1,0].tick_params(axis='x', rotation=45)
    
    # Statistical summary
    skewness = skew(train_data['SalePrice'])
    kurt = kurtosis(train_data['SalePrice'])
    log_skewness = skew(log_price)
    log_kurt = kurtosis(log_price)
    
    stats_text = f"""
    Original SalePrice:
    Skewness: {skewness:.3f}
    Kurtosis: {kurt:.3f}
    
    Log-Transformed:
    Skewness: {log_skewness:.3f}
    Kurtosis: {log_kurt:.3f}
    """
    
    axes[1,1].text(0.1, 0.5, stats_text, transform=axes[1,1].transAxes, 
                   fontsize=12, verticalalignment='center',
                   bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))
    axes[1,1].set_title('Distribution Statistics', fontweight='bold')
    axes[1,1].axis('off')
    
    # Correlation with key features
    key_features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath']
    correlations = [train_data[feat].corr(train_data['SalePrice']) for feat in key_features]
    
    axes[1,2].barh(key_features, correlations, color='lightgreen', alpha=0.8)
    axes[1,2].set_title('Correlation with Key Features', fontweight='bold')
    axes[1,2].set_xlabel('Correlation Coefficient')
    
    plt.tight_layout()
    plt.show()
    
    return log_price

# Apply log transformation to target variable
log_sale_price = analyze_target_distribution(combined_df)
