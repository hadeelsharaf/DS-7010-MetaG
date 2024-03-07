import streamlit as st
import pandas as pd

@st.cache_data
def get_bacteria_df():
    df_bacteria = pd.read_excel('Data Sheet 2.xlsx',
                                sheet_name='E_straw_Bac', skiprows=3, header=[0, 1, 2, 3])
    return df_bacteria

@st.cache_data
def get_fungi_df():
    """ updade sheet name and skiprows based on the data sheet 2.xlsx file"""
    df_fungi = pd.read_excel('Data Sheet 2.xlsx',
                             sheet_name='F_straw_Fungi', skiprows=3, header=[0, 1, 2, 3])
    return df_fungi


@st.cache_data
def transform_bacteria_data():
    df_bacteria = get_bacteria_df()
    df_bacteria.columns = ["_".join([str(index) for index in multi_index]) for multi_index in df_bacteria.columns.ravel()]
    df_bacteria = df_bacteria.iloc[:-1]
    # Step: Rename multiple columns
    df_bacteria = df_bacteria.rename(columns={'Domain_Unnamed: 0_level_1_Unnamed: 0_level_2_Unnamed: 0_level_3': 'Domain',
                                              'Phylum_Unnamed: 1_level_1_Unnamed: 1_level_2_Unnamed: 1_level_3': 'Phylum',
                                              'Class_Unnamed: 2_level_1_Unnamed: 2_level_2_Unnamed: 2_level_3': 'Class',
                                              'Order_Unnamed: 3_level_1_Unnamed: 3_level_2_Unnamed: 3_level_3': 'Order',
                                              'Family_Unnamed: 4_level_1_Unnamed: 4_level_2_Unnamed: 4_level_3': 'Family',
                                              'Genus_Unnamed: 5_level_1_Unnamed: 5_level_2_Unnamed: 5_level_3': 'Genus'})

    # Step: Replace missing values
    df_bacteria = df_bacteria.fillna('-')

    return df_bacteria

@st.cache_data
def tidy_bacteria_data():
    df_bacteria = transform_bacteria_data() 
    df_bacteria = df_bacteria.melt(id_vars=['Domain', 'Phylum', 'Class', 'Order', 'Family', 'Genus'])
    df_bacteria['location'] = df_bacteria['variable'].apply(lambda x: x.split('_')[0])
   
    df_bacteria['rotation'] = df_bacteria['variable'].apply(lambda x: x.split('_')[1])   
    df_bacteria['sample_type'] = df_bacteria['variable'].apply(lambda x: x.split('_')[2])
    df_bacteria['treatment'] = df_bacteria['variable'].apply(lambda x: x.split('_')[3])
    # remove spaces from the column treatment
    df_bacteria['treatment'] = df_bacteria['treatment'].str.strip()
    df_bacteria = df_bacteria.drop(columns=['variable'])
    return df_bacteria



@st.cache_data
def transform_fungi_data():
    df_fungi = get_fungi_df()
    df_fungi.columns = ["_".join([str(index) for index in multi_index]) for multi_index in df_fungi.columns.ravel()]
    df_fungi = df_fungi.iloc[:-1]
    # Step: Rename multiple columns
    df_fungi = df_fungi.rename(columns={'Phylum_Unnamed: 0_level_1_Unnamed: 0_level_2_Unnamed: 0_level_3': 'Phylum',
                                              'Class_Unnamed: 1_level_1_Unnamed: 1_level_2_Unnamed: 1_level_3': 'Class',
                                              'Order_Unnamed: 2_level_1_Unnamed: 2_level_2_Unnamed: 2_level_3': 'Order',
                                              'Family_Unnamed: 3_level_1_Unnamed: 3_level_2_Unnamed: 3_level_3': 'Family',
                                              'Genus_Unnamed: 4_level_1_Unnamed: 4_level_2_Unnamed: 4_level_3': 'Genus'})

    # Step: Replace missing values
    df_fungi = df_fungi.fillna('-')

    return df_fungi

@st.cache_data
def tidy_fungi_data():
    df_fungi = transform_fungi_data() 
    df_fungi = df_fungi.melt(id_vars=['Phylum', 'Class', 'Order', 'Family', 'Genus'])
    df_fungi['location'] = df_fungi['variable'].apply(lambda x: x.split('_')[0])
   
    df_fungi['rotation'] = df_fungi['variable'].apply(lambda x: x.split('_')[1])   
    df_fungi['sample_type'] = df_fungi['variable'].apply(lambda x: x.split('_')[2])
    df_fungi['treatment'] = df_fungi['variable'].apply(lambda x: x.split('_')[3])
    df_fungi['treatment'] = df_fungi['treatment'].str.strip()
    df_fungi = df_fungi.drop(columns=['variable'])
    return df_fungi