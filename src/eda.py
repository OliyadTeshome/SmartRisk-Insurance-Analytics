def clean_data(df):
    """
    Clean the insurance dataset by handling missing values and duplicates.
    
    Args:
        df (pd.DataFrame): Input dataframe to clean
        
    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    # Make a copy to avoid modifying original
    data = df.copy()
    
    # Drop columns with high missing values
    cols_to_drop = ['NumberOfVehiclesInFleet', 
                    'CrossBorder', 
                    'CustomValueEstimate', 
                    'Converted', 'Rebuilt', 
                    'WrittenOff']
    data = data.drop(columns=cols_to_drop)
    
    # Impute moderate missing data
    moderate_missing_cols = ['NewVehicle', 'Bank', 'AccountType']
    for col in moderate_missing_cols:
        if data[col].dtype == 'object':
            data[col] = data[col].fillna(data[col].mode()[0])
        else:
            data[col] = data[col].fillna(data[col].median())
            
    # Handle low missing data
    low_missing_cols = ['Gender', 'MaritalStatus', 'Cylinders', 'cubiccapacity', 
                       'kilowatts', 'NumberOfDoors', 'VehicleIntroDate', 'Model', 
                       'make', 'VehicleType', 'mmcode', 'bodytype', 'CapitalOutstanding']
    for col in low_missing_cols:
        if data[col].dtype == 'object':
            data[col] = data[col].fillna(data[col].mode()[0])
        else:
            data[col] = data[col].fillna(data[col].median())
            
    # Remove duplicates
    data = data.drop_duplicates()
    
    return data
