def apply_dimensionality_reduction(df):
    """Apply PCA and t-SNE for visualization and feature analysis"""
    
    # Select numerical features for PCA
    numerical_features = df.select_dtypes(include=[np.number]).columns
    feature_data = df[numerical_features].fillna(0)
    
    # Standardize features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(feature_data)
    
    # Apply PCA
    pca = PCA(n_components=0.95)  # Retain 95% variance
    pca_features = pca.fit_transform(scaled_features)
    
    # Create PCA visualization
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Explained variance plot
    cumsum_var = np.cumsum(pca.explained_variance_ratio_)
    axes[0].plot(range(1, len(cumsum_var) + 1), cumsum_var, 'bo-')
    axes[0].set_xlabel('Number of Components')
    axes[0].set_ylabel('Cumulative Explained Variance')
    axes[0].set_title('PCA: Cumulative Explained Variance')
    axes[0].grid(True)
    
    # Feature importance for first two components
    feature_importance = pd.DataFrame({
        'Feature': numerical_features,
        'PC1': pca.components_[0],
        'PC2': pca.components_[1]
    })
    
    top_features = feature_importance.iloc[np.argsort(np.abs(feature_importance['PC1']))[-10:]]
    axes[1].barh(range(len(top_features)), top_features['PC1'], alpha=0.7)
    axes[1].set_yticks(range(len(top_features)))
    axes[1].set_yticklabels(top_features['Feature'])
    axes[1].set_title('Top Features Contributing to PC1')
    
    plt.tight_layout()
    plt.show()
    
    return pca, pca_features

pca_model, pca_features = apply_dimensionality_reduction(combined_df)
