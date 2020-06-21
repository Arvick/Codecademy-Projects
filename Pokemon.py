class Pokemon:
  def __init__(self,name,level,typ,max_health,current_health,knocked_out,max_exp,current_exp,**evolution):
    self.name=name
    self.level=level
    self.type=typ
    self.max_health=max_health
    self.current_health=current_health
    self.knocked_out=knocked_out
    self.max_exp=max_exp
    self.current_exp=current_exp
    self.evol_list={}
    for evolution,req_level in evolution.items():
      self.evol_list[req_level]=evolution
      
      
  
  def __repr__(self):
    return("{name}".format(name=self.name))
  
  def stats(self):
    return("""{}'s stats:
Level:{} 
Type:{}
HP:{}
Possible Evolutions:{}
KO'd?:{}""".format(self.name,self.level,self.type,self.current_health,self.evol_list,self.knocked_out))
    
  def knockout(self):
    self.knocked_out=True
    return('{} has fainted! Please select another Pokemon using "Your Trainer Name".switch_active(Pokemon you wish to switch into).'.format(self))

  def lose_health(self,amnt,other):
    self.current_health-=amnt
    if self.current_health<= 0.0 or self.current_health<=0: 
      return('''{self} has lost {amount} HP! 
{dead}
{gain}'''.format(self=self,amount=amnt,dead=self.knockout(),gain=other.gain_exp((self.level*10//2))))
    else:
      return('{} has lost {} HP!'.format(self,amnt))    

  def regain_health(self,amnt):
    self.current_health+=amnt
    return('{} has gained {} health!'.format(self,amnt))

  def gain_exp(self,amnt):
    self.current_exp+=amnt
    if self.current_exp>=self.max_exp:
      return("{} has gained {} XP! {}".format(self,amnt,self.level_up()))
    else:
      return("{} has gained {} XP!".format(self,amnt))
  
  def level_up(self):
    if self.level!=100:
      self.level+=1
      if self.current_exp>self.max_exp:
        regen=self.current_exp-self.max_exp
        self.current_exp=0
        self.current_exp+=regen
      elif self.current_exp==self.max_exp:
        self.current_exp=0
      if self.evol_list.get(self.level)!=None:
        return("Congrats! Your {} is now level {} and is eligible for evolution! Use the 'Trainer Name'.update_pokemon(currentform, evolution) method if you wish to evolve your pokemon.".format(self, self.level))
      else:
        return("{} is now level {}!".format(self,self.level))
    else:
      return("This Pokemon cannot be leveled any further.")

      


    

  def attack(self,other):
    if self.knocked_out==False:
      if self.type=="Fire":
        if other.type=="Water":
          return("""{self} attacked {other}! It wasn't very effective... 
{lose}""".format(self=self,other=other,lose=other.lose_health(self.level/2,self)))
        elif other.type=="Grass":
          return("""{self} attacked {other}! It's super effective!
{lose}""".format(self=self,other=other,lose=other.lose_health(self.level * 2,self)))
        else:
          return("""{self} attacked {other}!
{lose}""".format(self=self,other=other,lose=other.lose_health(self.level,self)))

      elif self.type=="Water":
        if other.type=="Fire":
          return("""{self} attacked {other}! It wasn't very effective... 
{lose}""".format(self=self,other=other,lose=other.lose_health(self.level / 2,self)))
        elif other.type=="Grass":
          return("""{self} attacked {other}! It's super effective!
{lose}""".format(self=self,other=other,lose=other.lose_health(self.level * 2,self)))
        else:
          return("""{self} attacked {other}!
{lose}""".format(self=self,other=other,lose=other.lose_health(self.level,self)))

      else:
        if other.type=="Fire":
          return("""{self} attacked {other}! It wasn't very effective... 
{lose}""".format(self=self,other=other,lose=other.lose_health(self.level / 2,self)))
        elif other.type=="Water":
          return("""{self} attacked {other}! It's super effective!
{lose}""".format(self=self,other=other,lose=other.lose_health(self.level * 2,self)))
        else:
          return("""{self} attacked {other}!
{lose}""".format(self=self,other=other,lose=other.lose_health(self.level,self)))

    else:
      return("This Pokemon is fainted!")

class Trainer:
  def __init__(self, name, *pokemon,num_of_potions=0, currently_active=None):
    self.name=name
    self.pokemon=list(pokemon)
    self.num_of_potions=num_of_potions
    self.active=currently_active
    self.active=pokemon[0]
    
  def update_pokemon(self,replaced,new):
    temp=replaced.evol_list
    replaced.evol_list=(replaced.evol_list.items())
    replaced.evol_list=list(replaced.evol_list)
    a=[]
    for i in replaced.evol_list:
      for i in i:
        a.append(i)
    replaced.evol_list=temp
    if new.name in a:
      self.pokemon.remove(replaced)
      self.pokemon.append(new)
      a=list(replaced.evol_list.items())
      a.remove(a[0])
      new.evol_list={}
      for evo in a:
        for level, evo in a:
          new.evol_list[level]=evo
      return("{} has evolved into {}!".format(replaced,new))
    else:
      return("This evolution is of another Pokemon!")

  
  def __repr__(self):
    return("""
    Trainer {name}. 
    Pokemon in Party: {pokemon}. 
    Current Pokemon: {active}""".format(name=self.name,pokemon=self.pokemon,active=self.pokemon[0]))
  
  def use_potion(self,target):
    if target.knocked_out==False:
      if target in self.pokemon:
        if target.current_health!=target.max_health:
          self.num_of_potions-=1
          regen=20
          while target.current_health+regen>target.max_health:
            regen-=1
          HP=target.regain_health(regen)
          return("""{self} used a potion on {target}. 
  {potions} potions left. 
  {HP}""".format(self=self.name,target=target,        potions=self.num_of_potions,HP=HP))
        else:
          return("This Pokemon is already at full HP!")
      else:
        return("That Pokemon is not in your Party.")
    else:
      return("This Pokemon is fainted and cannot be healed!")


  
  def attack_trainer(self,opponent):
    return(self.active.attack(opponent.active))
    
  
  def switch_active(self,choice):
    if self.active!=choice:
      if choice.current_health !=0:
        former_active=self.active
        self.active=choice
        return("""Switching out {former} for {choice}....      Trainer {name} has brought out {choice}!""".format(former=former_active,choice=self.active,name=self.name))
      else:
        return('This Pokemon is fainted and cannot be switched in.')
    else:
      return("This Pokemon is already active!")

Charmeleon=Pokemon('Charmeleon',20,'Fire',125,125,False,100,0)
Charizard=Pokemon('Charizard',45,'Fire',150,150,False,300,0)
Charmander=Pokemon('Charmander',1,'Fire',100,100,False,50,0,**{Charmeleon.name:20,Charizard.name:45})

Ivysaur=Pokemon('Ivysaur',20,'Grass',125,125,False,100,0)
Venausaur=Pokemon('Venausaur',45,'Grass',150,150,False,300,0)
Bulbasaur=Pokemon('Bulbasaur',1,'Grass',100,100,False,50,0,**{Ivysaur.name:20,Venausaur.name:45})

red_pokemon=[Charmander,Bulbasaur]


Red=Trainer('Red',*red_pokemon,num_of_potions=4)

Wartortle=Pokemon('Wartortle',20,'Water',125,125,False,100,0)
Blastoise=Pokemon('Blastoise',45,'Water',150,150,False,300,0)
Squirtle=Pokemon('Squirtle',1,'Water',100,1,False,50,0,**{Wartortle.name:20,Blastoise.name:45})

blue_pokemon=[Squirtle]
Blue=Trainer('Blue',*blue_pokemon,num_of_potions=4)






