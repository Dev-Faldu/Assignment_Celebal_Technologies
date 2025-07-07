def create_neighborhood_clusters(df, n_clusters=5):
    """Create neighborhood clusters based on price patterns"""
    
    # Calculate neighborhood statistics
    train_data = df[df['SalePrice'].notna()]
    neighborhood_stats = train_data.groupby('Neighborhood')['SalePrice'].agg([
        'mean', 'median', 'std', 'count'
    ]).reset_index()
    
    # Apply K-means clustering
    features_for_clustering = ['mean', 'median', 'std']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(neighborhood_stats[features_for_clustering])
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    neighborhood_stats['PriceCluster'] = kmeans.fit_predict(scaled_features)
    
    # Map clusters back to original data
    cluster_map = dict(zip(neighborhood_stats['Neighborhood'], 
                          neighborhood_stats['PriceCluster']))
    df['NeighborhoodCluster'] = df['Neighborhood'].map(cluster_map)
    
    return df, neighborhood_stats

combined_df, neighborhood_clusters = create_neighborhood_clusters(combined_df)
