class player:
  def play(self):
    print("The player is playing cricket.")
class Batsman(player):
   def play(self):
     print("The bastman is batting.")
class Bowler(player):
   def play(self):
     print("The bowling is bowling.")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()
