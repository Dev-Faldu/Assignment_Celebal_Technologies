def apply_skewness_correction(df, threshold=0.75):
    """Apply log transformation to highly skewed numerical features"""
    
    numerical_features = df.select_dtypes(include=[np.number]).columns
    skewed_features = []
    
    for feature in numerical_features:
        if feature not in ['Id', 'SalePrice', 'is_train']:
            skewness = skew(df[feature].dropna())
            if abs(skewness) > threshold:
                skewed_features.append((feature, skewness))
                # Apply log1p transformation (handles zeros)
                df[f'{feature}_log'] = np.log1p(df[feature])
    
    return skewed_features

skewed_features = apply_skewness_correction(combined_df)
