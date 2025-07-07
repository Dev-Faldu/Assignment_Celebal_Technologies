def detect_and_handle_outliers(df, method='iqr', threshold=1.5):
    """Detect outliers using IQR or Z-score methods"""
    
    train_data = df[df['SalePrice'].notna()].copy()
    outlier_indices = set()
    
    # Key features for outlier detection
    key_features = ['GrLivArea', 'TotalBsmtSF', 'LotArea', 'SalePrice']
    
    for feature in key_features:
        if method == 'iqr':
            Q1 = train_data[feature].quantile(0.25)
            Q3 = train_data[feature].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            
            feature_outliers = train_data[
                (train_data[feature] < lower_bound) | 
                (train_data[feature] > upper_bound)
            ].index
            
        elif method == 'zscore':
            z_scores = np.abs(stats.zscore(train_data[feature]))
            feature_outliers = train_data[z_scores > threshold].index
        
        outlier_indices.update(feature_outliers)
    
    # Visualize outliers
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    for i, feature in enumerate(['GrLivArea', 'TotalBsmtSF']):
        row, col = i // 2, i % 2
        
        # Scatter plot with outliers highlighted
        normal_data = train_data[~train_data.index.isin(outlier_indices)]
        outlier_data = train_data[train_data.index.isin(outlier_indices)]
        
        axes[row, col].scatter(normal_data[feature], normal_data['SalePrice'], 
                              alpha=0.6, color='blue', label='Normal')
        axes[row, col].scatter(outlier_data[feature], outlier_data['SalePrice'], 
                              alpha=0.8, color='red', label='Outliers')
        axes[row, col].set_xlabel(feature)
        axes[row, col].set_ylabel('SalePrice')
        axes[row, col].set_title(f'{feature} vs SalePrice')
        axes[row, col].legend()
    
    plt.tight_layout()
    plt.show()
    
    return list(outlier_indices)

outlier_indices = detect_and_handle_outliers(combined_df)
