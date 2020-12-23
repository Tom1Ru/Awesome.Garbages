#Atsuki Tomita
#2020-12-23
#info2 on SFC


import pyxel,random,math

#App全体のクラスを作成
class App:
    #システム全容を把握
    def __init__(self):
        pyxel.init(120,240)
        self.notes = []
        self.score = 0
        self.life = 10
        self.gameover = False
        pyxel.run(self.update,self.draw)

    #画面をUPDATE
    def update(self):
        if not self.gameover:
            Note.speed = math.log(pyxel.frame_count)
            a = random.randint(0,90)
            if a < math.log(pyxel.frame_count):
                self.notes.append(Note())

            #ノーツが降ってきたらボタンを押そうね
            #ひとつにつき1000pointね
            for i in self.notes:
                i.move()
                #当たり判定キツかったらここで調整s
                if pyxel.btnp(pyxel.KEY_D) and i.x == 0 and 200 < i.y < 220:
                    self.score += 1000
                    self.notes.remove(i)
                    return
                
                if pyxel.btnp(pyxel.KEY_F) and i.x == 1 and 200 < i.y < 220:
                    self.score += 1000
                    self.notes.remove(i)
                    return

                if pyxel.btnp(pyxel.KEY_J) and i.x == 2 and 200 < i.y < 220:
                    self.score += 1000
                    self.notes.remove(i)
                    return

                if pyxel.btnp(pyxel.KEY_K) and i.x == 3 and 200 < i.y < 220:
                    self.score += 1000
                    self.notes.remove(i)
                    return

                #バーのラインを超えたらライフが減るよ
                if i.y > 240:
                    self.life -= 1
                    if self.life == 0:
                        self.gameover = True
                    self.notes.remove(i)
                    return
            
        #ゲームオーバーになったらエンター押してやり直せ
        else:
            if pyxel.btnp(pyxel.KEY_ENTER):
                self.life = 10
                self.score = 0
                self.notes.clear()
                Note.speed = 0
                self.gameover = False

    #描写
    def draw(self):
        if not self.gameover:
            pyxel.cls(7)
            pyxel.rect(0,205,120,5,0)
            for i in self.notes:
                i.show()
            pyxel.text(50,185,"score:"+str(self.score),0)
            pyxel.text(50,195,"life:"+str(self.life),0)

        #ゲームオーバー表示
        else:
            pyxel.text(50,150,"NOWAY....",8)
            pyxel.text(50,175,"GAME OVER",8)


#ノーツ
class Note:
    speed = 0
    def __init__(self):
        self.x = random.randint(0,3)
        self.y = 0

    #落ちてこいノーツ
    def move(self):
        self.y += Note.speed

    
    def show(self):
        pyxel.rect(self.x*30,self.y-5,30,5,6)

App()


#This program is using Pyxel game engine.[https://github.com/kitao/pyxel]
#Thanks for Mr.3D Mask's support.
