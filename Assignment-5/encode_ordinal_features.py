def encode_ordinal_features(df):
    """Encode quality-based features as ordinal variables"""
    
    # Quality mappings
    quality_map = {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'None': 0}
    
    quality_features = ['ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 
                       'HeatingQC', 'KitchenQual', 'FireplaceQu', 
                       'GarageQual', 'GarageCond', 'PoolQC']
    
    for feature in quality_features:
        if feature in df.columns:
            df[f'{feature}_ord'] = df[feature].map(quality_map)
    
    # Basement finish mappings
    bsmt_fin_map = {'GLQ': 6, 'ALQ': 5, 'BLQ': 4, 'Rec': 3, 'LwQ': 2, 'Unf': 1, 'None': 0}
    
    for feature in ['BsmtFinType1', 'BsmtFinType2']:
        if feature in df.columns:
            df[f'{feature}_ord'] = df[feature].map(bsmt_fin_map)
    
    # Garage finish mapping
    garage_fin_map = {'Fin': 3, 'RFn': 2, 'Unf': 1, 'None': 0}
    if 'GarageFinish' in df.columns:
        df['GarageFinish_ord'] = df['GarageFinish'].map(garage_fin_map)
    
    return df

combined_df = encode_ordinal_features(combined_df)
