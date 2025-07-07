def create_aggregate_features(df):
    """Create meaningful aggregate features"""
    
    # Total square footage
    df['TotalSF'] = df['TotalBsmtSF'] + df['1stFlrSF'] + df['2ndFlrSF']
    
    # Total bathrooms
    df['TotalBath'] = (df['FullBath'] + 
                       df['HalfBath'] * 0.5 + 
                       df['BsmtFullBath'] + 
                       df['BsmtHalfBath'] * 0.5)
    
    # Total porch area
    df['TotalPorchSF'] = (df['OpenPorchSF'] + 
                          df['EnclosedPorch'] + 
                          df['3SsnPorch'] + 
                          df['ScreenPorch'])
    
    # Binary indicators
    df['HasPool'] = (df['PoolArea'] > 0).astype(int)
    df['HasGarage'] = (df['GarageArea'] > 0).astype(int)
    df['HasBasement'] = (df['TotalBsmtSF'] > 0).astype(int)
    df['HasFireplace'] = (df['Fireplaces'] > 0).astype(int)
    df['Has2ndFloor'] = (df['2ndFlrSF'] > 0).astype(int)
    df['HasWoodDeck'] = (df['WoodDeckSF'] > 0).astype(int)
    
    # Age-related features
    df['HouseAge'] = df['YrSold'] - df['YearBuilt']
    df['RemodAge'] = df['YrSold'] - df['YearRemodAdd']
    df['GarageAge'] = df['YrSold'] - df['GarageYrBlt']
    
    # Quality scores
    df['OverallScore'] = df['OverallQual'] * df['OverallCond']
    
    return df

combined_df = create_aggregate_features(combined_df)
