#!/usr/bin/env python
# coding: utf-8

# # Proyek Analisis Data: [Input Nama Dataset]
# - **Nama:** Rafi Iyad Madani Chaidir
# - **Email:** rafiiyad2004@gmail.com
# - **ID Dicoding:** rafi_iyad

# ## Menentukan Pertanyaan Bisnis

# - Apakah ada perbedaan dalam jumlah peminjaman sepeda pada hari libur dibandingkan dengan hari biasa?
# - Apakah terdapat perbedaan dalam pola peminjaman sepeda antara musim-musim tertentu?
# -  Bagaimana cuaca memengaruhi jumlah peminjaman sepeda?

# ## Import Semua Packages/Library yang Digunakan

# In[141]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## Data Wrangling

# ### Gathering Data

# In[142]:


day = pd.read_csv("day.csv")
hour = pd.read_csv("hour.csv")


# Memasukkan Data Set Day dan Hour

# ### Assessing Data

# Memahami Data set yang telah di masukkan menggunakan `head()`,`info()`

# In[64]:


hour.head()


# In[65]:


print(hour.info())


# Tak lupa juga untuk mengecek Missing Value menggunakan `isna().sum()` dan mengecek data duplikat menggunakan `duplicated().sum()`

# In[66]:


hour.isna().sum()


# In[67]:


print("Jumlah duplikasi: ", hour.duplicated().sum())


# In[68]:


hour.describe()


# In[69]:


day.head()


# In[70]:


day.info()


# In[71]:


day.isna().sum()


# In[72]:


day.duplicated().sum()


# In[73]:


day.describe()


# Setelah dipahami menggunakan `descibe()`. Data Day dan Hour tidak memiliki Keanehan dan Normal

# ### Cleaning Data

# Saya membuat dataframe baru yang menghapus fitur instant dan windspeed karena fitur tersebut kami tidak gunakan

# In[96]:


cleaned_day = day.drop(labels=['instant', 'windspeed'], axis=1)


# In[97]:


cleaned_day.head()


# Agar mudah dipahami, saya akan mengubah isi datanya menjadi kategorial

# In[145]:


cleaned_day['yr'] = cleaned_day['yr'].replace({0: 2011, 1: 2012})

season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
cleaned_day['season'] = cleaned_day['season'].replace(season_mapping)

weather_mapping = {
    1: 'Clear/Cloudy',
    2: 'Mist/Cloudy',
    3: 'Light Snow/Light Rain/Cloudy',
    4: 'Extreme Weather'
}
cleaned_day['weathersit'] = cleaned_day['weathersit'].replace(weather_mapping)

month_mapping = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
}
cleaned_day['mnth'] = cleaned_day['mnth'].replace(month_mapping)

weekday_mapping = {
    0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'
}
cleaned_day['weekday'] = cleaned_day['weekday'].replace(weekday_mapping)


# In[146]:


cleaned_day.head()


# ## Exploratory Data Analysis (EDA)

# ### Explore cleaned_day

# In[124]:


cleaned_day[cleaned_day['holiday'] == 1]['cnt'].describe()


# In[123]:


cleaned_day[cleaned_day['holiday'] == 0]['cnt'].describe()

Dari hasil analisis di atas, terlihat bahwa terdapat perbedaan dalam jumlah peminjaman sepeda antara musim-musim tertentu. Rata-rata jumlah peminjaman sepeda tertinggi terjadi pada musim Fall (rata-rata sekitar 5644), diikuti oleh musim Summer (rata-rata sekitar 4992), Winter (rata-rata sekitar 4728), dan Spring (rata-rata sekitar 2604). Hal ini mengindikasikan bahwa musim tertentu dapat memengaruhi pola peminjaman sepeda secara signifikan.
# In[125]:


cleaned_day.groupby('season')['cnt'].describe()


# Dalam hasil diatas, menunjukkan musim semi memiliki rata-rata peminjaman sepeda yang lebih rendah, mungkin karena cuaca yang belum sepenuhnya stabil atau faktor-faktor lain yang mempengaruhi minat masyarakat untuk bersepeda.

# In[148]:


cleaned_day.groupby('weathersit')['cnt'].describe()


#  Hari-hari dengan cuaca cerah atau berawan memiliki jumlah peminjaman sepeda tertinggi, dengan rata-rata sekitar 4876. 

# ## Visualization & Explanatory Analysis

# ### Pertanyaan 1: Apakah ada perbedaan dalam jumlah peminjaman sepeda pada hari libur dibandingkan dengan hari biasa?

# In[152]:


plt.figure(figsize=(8, 6))
sns.barplot(x='holiday', y='cnt', data=cleaned_day, errcolor=None)
plt.title('Average Bike Rental Count by Holiday')
plt.xlabel('Holiday')
plt.ylabel('Average Bike Rental Count')
plt.xticks([0, 1], ['Regular Day', 'Holiday'])
plt.show()


# Hasil analisis tersebut menunjukkan Hari biasa paling banyak terjadi pemimnjaman sepeda

# ### Pertanyaan 2: Apakah terdapat perbedaan dalam total peminjaman sepeda antara musim-musim tertentu?

# In[153]:


# Plot rata-rata jumlah peminjaman sepeda berdasarkan musim
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=cleaned_day, estimator='mean')
plt.title('Average Bike Rental Count by Season')
plt.xlabel('Season')
plt.ylabel('Average Bike Rental Count')
plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])
plt.show()


# Berdasarkan analisis yang dilakukan menunjukkan bahwa Musim Semi memiliki rata rata peminjaman sepeda yang tertinggi diikuti oleh Musim Panas, Musim Winter dan Musim Spring. Hal ini menunjukkan bahwa benar musim sangatlah mempengaruhi jumlah peminjam sepeda

# ## Pertanyaan 3 : Bagaimana cuaca memengaruhi jumlah peminjaman sepeda?

# In[154]:


plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=cleaned_day, estimator='mean')
plt.title('Average Bike Rental Count by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Average Bike Rental Count')
plt.xticks([0, 1, 2, 3], ['Clear', 'Mist', 'Light Snow/Rain', 'Heavy Rain/Snow'])
plt.show()


# Hal ini menunjukkan bahwa kondisi cuaca sangatlah mempengaruhi total peminjaman sepeda

# ## Conclusion

# - Conclution pertanyaan 1
# 
# Dari hasil analisis, terlihat bahwa jumlah peminjaman sepeda pada hari biasa (non-holiday) lebih tinggi dibandingkan dengan hari libur (holiday). Hal ini menunjukkan bahwa mayoritas peminjaman sepeda terjadi pada hari-hari biasa, yang mungkin disebabkan oleh aktivitas sehari-hari seperti pergi ke tempat kerja atau sekolah. Oleh karena itu, dapat disimpulkan bahwa hari biasa cenderung menjadi periode di mana peminjaman sepeda paling banyak terjadi
# 
# - Conclution pertanyaan 2
# 
# Hasil Analisis mengatakan bahwa musim memiliki pengaruh signifikan terhadap jumlah peminjaman sepeda. Musim semi menunjukkan rata-rata peminjaman sepeda tertinggi, diikuti oleh musim panas, musim dingin, dan musim semi secara berurutan. Hal ini menunjukkan bahwa perubahan musim memengaruhi minat masyarakat dalam menggunakan sepeda, dengan tingkat peminjaman yang lebih tinggi terjadi pada musim yang lebih hangat dan cerah. Dengan demikian, kesimpulan ini memberitahu pentingnya faktor cuaca dan musim dalam memprediksi pola peminjaman sepeda.
# 
# - Conclution Pertanyaan 3 
# 
# Dengan analisis yang telah dilakukan menunjukkan  bahwa kondisi cuaca memiliki pengaruh yang signifikan terhadap jumlah total peminjaman sepeda. Kondisi cuaca yang baik, seperti cuaca cerah dan bersih, cenderung meningkatkan jumlah peminjaman sepeda, sedangkan kondisi cuaca buruk, seperti hujan atau salju, cenderung mengurangi jumlah peminjaman sepeda. Hal ini menunjukkan bahwa keputusan untuk meminjam sepeda dipengaruhi oleh kondisi cuaca saat itu.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
