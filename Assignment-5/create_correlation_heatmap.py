def create_correlation_heatmap(df):
    """Generate comprehensive correlation analysis"""
    
    # Select numerical features only
    numerical_df = df.select_dtypes(include=[np.number])
    
    # Calculate correlation matrix
    corr_matrix = numerical_df.corr()
    
    # Create correlation heatmap
    plt.figure(figsize=(20, 16))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    
    sns.heatmap(corr_matrix, mask=mask, annot=False, cmap='coolwarm', center=0,
                square=True, cbar_kws={'shrink': 0.8})
    plt.title('Feature Correlation Matrix', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    # Identify highly correlated features (|correlation| > 0.8)
    high_corr_pairs = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            if abs(corr_matrix.iloc[i, j]) > 0.8:
                high_corr_pairs.append({
                    'Feature_1': corr_matrix.columns[i],
                    'Feature_2': corr_matrix.columns[j],
                    'Correlation': corr_matrix.iloc[i, j]
                })
    
    return pd.DataFrame(high_corr_pairs)

high_corr_features = create_correlation_heatmap(combined_df)
