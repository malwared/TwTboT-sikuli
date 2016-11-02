Settings.MoveMouseDelay = 0.0
ArrayForMyBot = ('#test1','#test2','#test3','#test4','#test5')

def follow():
  #  click("1478013480715.png") 
 #   sleep(2)
    for f in ArrayForMyBot:
        if exists("search.png"):
            click("search-1.png")
            type(f)
            click(Pattern("searchbro.png").targetOffset(2,0))
            sleep(2)
            click(Pattern("bar-1.png").targetOffset(-177,4))
            sleep(3)
            wait("rt-1.png")
            click("rt-2.png")
            wait("type.png")
            sleep(2)
            click("type.png")
            
            type(f+" Follow me")
            
            click("cdsas.png")            
            
          
            sleep(2)
            click(Pattern("home13.png").targetOffset(-111,2))
        else:
            follow()
follow()
      
