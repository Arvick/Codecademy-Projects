# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages):
  newdam=[]
  for damage in damages:
    if damage=='Damages not recorded':
      newdam.append(damage)
    else:
      if damage.find('M')!=-1:
        damage=damage[:len(damage)-1]
        newdam.append((float(damage)*1000000))
      elif damage.find('B')!=-1:
        damage=damage[:len(damage)-1]
        newdam.append((float(damage)*1000000000))
  return(newdam)
newdam=update_damages(damages)






# write your construct hurricane dictionary function here:
def hurricane_dict(names,months,years,max_sustained_winds,areas_affected,newdam,deaths):
  newdict={}
  for i in range(0,34):
    newdict[names[i]]={'Name':names[i],'Month':months[i],'Year':years[i],'Max Sustained Wind':max_sustained_winds[i],'Areas Affected':areas_affected[i],'Damages':newdam[i],'Deaths':deaths[i]}
  return(newdict)

# write your construct hurricane by year dictionary function here:
def organize_year(inptyear=None,**dic):
  try:
    year_dict={}
    for value in dic.values():
      temp={}
      temp=dict(value.items())
      year= temp['Year']
      if year not in year_dict.keys():
        year_dict[year]=[]
        year_dict[year].append(temp)
      else:
        year_dict[year].append(temp)
    if inptyear==None:
      return(year_dict)
    return(year_dict[inptyear])
  except KeyError:
    return("That year has no recorded data.")

# write your count affected areas function here:
def affected_areas(**dic):
  area_dict={}
  for value in dic.values():
    temp={}
    temp=dict(value.items())
    area=temp['Areas Affected']
    for area in area:
      if area not in area_dict.keys():
        area_dict[area]=1
      else:
        area_dict[area]+=1
  return(area_dict)






# write your find most affected area function here:
def most_affected(**dic):
  dic=affected_areas(**dic)
  greatest=0
  mostarea=""
  for area, count in dic.items():
    if count>greatest:
      mostarea=area
      greatest=count
  return(mostarea,greatest)





# write your greatest number of deaths function here:
def death_count(**dic):
  death_dict={}
  for value in dic.values():
    temp=dict(value.items())
    death_dict[temp['Name']]=temp['Deaths']
  area=""
  most=0
  for area,count in death_dict.items():
    if count>most:
      most=count
      area=area
  return(area,most)

  






# write your catgeorize by mortality function here:
def mortality_scale(**dic):
  mortality_scale = {0:[],1:[],2:[], 3:[], 4:[],5:[]}
  for value in dic.values():
    temp=dict(value.items())
    if temp['Deaths'] in range(1,101):
      mortality_scale[1].append(temp['Name'])
    elif temp['Deaths'] in range(100,501):
        mortality_scale[2].append(temp['Name'])
    elif temp['Deaths'] in range(500,1001):
        mortality_scale[3].append(temp['Name'])
    elif temp['Deaths'] in range(1000,10001):
       mortality_scale[4].append(temp['Name'])
    elif temp['Deaths'] >10000:
        mortality_scale[5].append(temp['Name'])
    else:
      mortality_scale[0].append(temp['Name'])
  return(mortality_scale)
      
      






# write your greatest damage function here:
def greatest_damage(**dic):
  mostdamage=0
  name=''
  for value in dic.values():
    temp=dict(value.items())
    if temp['Damages']!='Damages not recorded':
      if temp['Damages']>mostdamage:
        mostdamage=temp['Damages']
        name=temp['Name']
  return(name,mostdamage)








# write your catgeorize by damage function here:
def damage_scale(**dic):
  damage_scale = {'Unknown':[],1:[],2:[], 3:[], 4:[],5:[]}
  for value in dic.values():
    temp=dict(value.items())
    if temp['Damages']!='Damages not recorded':
      if int(temp['Damages']) in range(1,100000001):
        damage_scale[1].append(temp['Name'])
      elif int(temp['Damages']) in range(100000000,1000000001):
          damage_scale[2].append(temp['Name'])
      elif int(temp['Damages']) in range(1000000000,10000000001):
          damage_scale[3].append(temp['Name'])
      elif int(temp['Damages']) in range(10000000000,50000000001):
        damage_scale[4].append(temp['Name'])
      elif int(temp['Damages']) >50000000000:
          damage_scale[5].append(temp['Name'])
    else:
      damage_scale['Unknown'].append(temp['Name'])
  return(damage_scale)






dic=hurricane_dict(names,months,years,max_sustained_winds,areas_affected,newdam,deaths)

print(organize_year(**dic))




