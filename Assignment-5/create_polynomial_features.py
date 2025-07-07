def create_polynomial_features(df):
    """Create polynomial and interaction features"""
    
    # Polynomial features for key variables
    df['OverallQual_sq'] = df['OverallQual'] ** 2
    df['OverallQual_cb'] = df['OverallQual'] ** 3
    df['GrLivArea_sq'] = df['GrLivArea'] ** 2
    
    # Interaction features
    df['GrLivArea_x_OverallQual'] = df['GrLivArea'] * df['OverallQual']
    df['GrLivArea_x_TotalBsmtSF'] = df['GrLivArea'] * df['TotalBsmtSF']
    df['BsmtFinSF1_x_BsmtFinSF2'] = df['BsmtFinSF1'] * df['BsmtFinSF2']
    df['GarageArea_x_GarageCars'] = df['GarageArea'] * df['GarageCars']
    
    # Ratio features
    df['LivArea_to_LotArea'] = df['GrLivArea'] / (df['LotArea'] + 1)
    df['BsmtRatio'] = df['TotalBsmtSF'] / (df['GrLivArea'] + 1)
    df['GarageRatio'] = df['GarageArea'] / (df['GrLivArea'] + 1)
    
    return df

combined_df = create_polynomial_features(combined_df)
