# https://leetcode-cn.com/contest/sf-2020/problems/werewolves-of-leetcode/

# 小李的同事们很喜欢玩狼人杀，每次都找他当法官。小李觉得很累，决定写一个程序来跑出狼人杀的结果。

# 狼人杀是一个桌游。常见局由 12 名玩家和 1 名法官组成。12 名玩家坐成一个圈。每个玩家在游戏开始时随机抽取一张角色卡牌，只能知道自己的身份。 玩家分为两个阵营，狼人和村民。

# 狼人的胜利条件是 狼人阵营的玩家数 >= 村民阵营的玩家数
# 村民的胜利条件是 所有狼人出局
# 游戏过程

# 游戏分为夜晚和白天。

# (夜晚) 拿到狼人身份的玩家睁眼，其他人闭眼。狼人们商量后选择一名玩家击杀；
# (白天) 所有人睁眼；
# 法官宣布昨晚出局的玩家，以及熊是否咆哮了；
# 出局的玩家离开游戏，发动技能（如果有）；
# 法官检查胜利条件，如果任何一个满足则结束游戏；
# 在场玩家进行一轮发言，并票选最可疑的玩家出局；
# 被选中的玩家离开游戏，发动技能（如果有）；
# 法官检查胜利条件，如果任何一个满足则结束游戏；
# 重复 1；
# 游戏角色
# 【村民阵营】x8

# 村民(villager, 下称"vil") x5：没有特殊技能
# 猎人("hunter") x1：技能是在出局时（被投票或被狼人击杀）可以向所有人亮出底牌选择带走一名玩家
# 白痴("idiot") x1：技能是在白天被投票出局后自动亮出底牌并且不出局
# 驯熊人(bear tamer, 下称"bear") x1：（简称熊）每天夜里，如果相邻两名存活玩家有任何一个是狼人，熊会发出咆哮。如果驯熊人已经死亡，则这一局熊不再咆哮。驯熊人如果当晚被杀，熊也不会咆哮。（相邻指向左找第一名存活玩家和向右找第一名存活玩家，当晚被杀的玩家也视为死亡）
# 【狼人阵营】x4

# 狼人(werewolf, 下称"ww") x4：可以知道同伴，但不知道好人的具体角色。
# 对于所有人：

# 白天可以投票
# 除了发言的环节，玩家不能发言或者交换信息
# 模拟器设定

# 我们用 c 来模拟每名玩家在游戏开始时在他人眼中的可信度。0 < c < 100 。越小则越像狼人
# 狼人只击杀非狼人，并且在场玩家知晓这点
# 在投票环节，c 最低的玩家出局。如果有多个目标，则座位号小号出局。
# 狼人优先击杀熊，其他时候击杀 c 最高的好人（村民阵营），如果有多个目标，则击杀座位号小号。
# 玩家的 c 变成 0 或者 100 表示已知身份： 铁狼 或者 铁好人
# 玩家的 c 会根据大家获取到的信息发生改变，所有人看到的可信度 c 一起更新。注意，改变的时机需要遵守游戏过程：
# 猎人出局或白痴被投票出局时一定发动技能，使 ta 的 c 变为 100；猎人会射杀 c 最低的玩家，如果有多个目标，则射杀座位号小号
# 第一天发言时，如果驯熊人依然存活，驯熊人会公布身份，使 ta 的 c 变为 100（在模拟器中狼不会假装自己是熊）
# 如果熊咆哮了，人们开始怀疑其左右的未知身份玩家，这使他们的 c 变为原来的一半 (向下取整, 如果原来是 1 则不变 )
# 如果熊咆哮了且左右的在局一方为铁好人，则另一方成为铁狼；如果其中一方后来被发现是铁好人，人们也会更新另一方的 c 
# 如果熊在场且没有咆哮，则左右的在场玩家成为铁好人
# 如果驯熊人在第一次发言前死亡，则场上玩家不知道其位置，也无法利用熊的咆哮信息
# 如果玩家在夜间死亡，则该离场的玩家也被认为是铁好人
# 输入：

# players：一个长度为 12 的 string 数组，坐标代表座位，字符串代表底牌, 有以下可能："vil", "hunter", "idiot", "bear" 和 "ww"。 其中 "vil" 会出现 5 次， "ww"会出现 4 次， 其他每个都是 1 次。 坐标 0 和 11 也视为相邻。

# credibility：一个长度为 12 的 int 数组，坐标代表座位，int 代表玩家初始的可信度

# 输出：

# 根据模拟器的设定，村民阵营是否能赢

# 示例 1：

# Input: players = ["bear","vil","vil","ww","vil","vil","idiot","ww","hunter","ww","ww","vil"], credibility = [9,55,62,74,43,70,13,23,15,78,61,66]
# Output: false
# 解释：

# 第一天夜晚，狼人击杀玩家 5，熊没有咆哮。

# 第二天白天，玩家 0 公布自己熊的身份。玩家 1 和玩家 11 成为 铁好人。看上去最可疑的玩家 6 被投出，但是因为是 白痴 身份，并没有出局。玩家 6 成为 铁好人。

# 第二天夜晚，狼人击杀玩家 0 驯熊人。熊没有咆哮。

# 第三天白天，身份最低的玩家 8 猎人被投票出局。猎人选择带走场上可信度最低的玩家 7。

# 第三天夜晚，狼人击杀身份最高的玩家 1 村民。

# 第四天白天，身份最低的玩家 4 村民被投票出局。

# 第四天夜晚，狼人击杀玩家 6 白痴, 此时场上狼人数量等于好人数量，狼人胜利。

 

# 示例 2：

# Input: players = ["vil", "vil", "vil", "ww", "vil", "ww", "ww", "vil", "ww", "bear", "hunter", "idiot"], credibility = [81, 71, 88, 31, 34, 40, 70, 94, 73, 79, 98, 48]
# Output: true
# 解释：

# 第一回合猎人出局，熊咆哮了，但由于熊没有跳身份，对于猎人是无效信息，不能更新 c ，猎人击杀 3 号位玩家狼人。本回合投票投出 11 号白痴，白痴亮出身份牌， c 变为 100 。

 

# 示例 3：

# Input: players = ["vil","ww","bear","hunter","ww","idiot","vil","vil","ww","vil","ww","vil"], credibility = [45,67,32,25,1,27,99,85,3,54,3,25]
# Output: true
# 解释：

# 最后一轮投票，猎人被投出，发动技能。由于此时猎人已经是铁好人，通过第一轮熊咆哮可以得出 1 号位是铁狼，所以本轮猎人击杀 1 号位狼人，游戏结束，村民胜利。

from typing import List



class Solution:
   bearSide = []

   def canVillagersWin(self, players: List[str], credibility: List[int]) -> bool:
      lastKilled = -1      

      # -1 狼赢  1 好人赢 0 继续
      def checkEnd(): 
         ww_num = players.count('ww')
         if ww_num == 0 : # 狼没了
            return 1
         elif ww_num >= (12- ww_num - players.count('dead')):
            return -1
         else:
            return 0
         
      def isGameOver():
         return checkEnd() != 0
      
      def findMin():
         m = 13
         minCred = 101
         for i in range(12):
            if players[i] != 'dead':
               if credibility[i] < minCred:
                  minCred = credibility[i]
                  m = i
         return m
      
      def night():
         maxCred = -1
         for i in range(12):
            if players[i] == 'show_bear':
               return i
            elif players[i] != 'ww' and players[i] != 'dead':
               if credibility[i] > maxCred:
                  lastKilled = i
                  maxCred = credibility[i]
         
         return lastKilled

      def bearSkill():
         for i in range(12):
            if players[i] == 'bear':
               credibility[i] = 100
               players[i] = 'show_bear'

               l = (i-1) % 12 
               if l == lastKilled:
                  l = (l-1) % 12 

               r = (i+1) % 12
               if r == lastKilled:
                  r = (r+1) % 12 



               if players[l] == 'ww' or players[r] == 'ww':
                  Solution.bearSide = [l, r]
                  credibility[l] = 100 if credibility[l] == 100 else credibility[l] >> 1
                  credibility[r] = 100 if credibility[r] == 100 else credibility[r] >> 1
               else :
                  credibility[l] = 100
                  credibility[r] = 100
               
               break


      def updateBearSide(deadIndex):
         if len(Solution.bearSide) < 2 :
            return
         if Solution.bearSide[0] == deadIndex:
            credibility[Solution.bearSide[1]] = 0
         elif Solution.bearSide[1] == deadIndex:
            credibility[Solution.bearSide[0]] = 0

      def day():
         # 处理昨夜死亡
         role = players[lastKilled] 
         print('kill : ', lastKilled)
         players[lastKilled] = 'dead'
         credibility[lastKilled] = 100
         updateBearSide(lastKilled)

         if isGameOver():
            return
         else :
            if role == 'hunter':
               m = findMin()
               players[m] = 'dead'
               print('shoot : ', m)
               if isGameOver():
                  return
            
            bearSkill()
         
            
            voted = findMin()
            if players[voted] == 'idiot':
               credibility[voted] = 100
               updateBearSide(voted)
               print('vote idiot : ', voted)

            else :
               votedType = players[voted]
               players[voted] = 'dead'
               print('vote : ', voted)
               if isGameOver():
                  return
               if votedType == 'hunter':
                  credibility[voted] = 100
                  updateBearSide(voted)
                  m = findMin()
                  players[m] = 'dead'
                  print('shoot : ', m)

      isNight = True
      while not isGameOver():
         if isNight:
            lastKilled = night()
            isNight = False
         else :
            day()
            isNight = True
      
      print('================', checkEnd() == 1 ,'================')
      return checkEnd() == 1


# Solution().canVillagersWin(["bear", "vil", "vil", "ww", "vil", "vil", "idiot", "ww", "hunter", "ww", "ww", "vil"], [9, 55, 62, 74, 43, 70, 13, 23, 15, 78, 61, 66])

# Solution().canVillagersWin(["vil", "vil", "vil", "ww", "vil", "ww", "ww", "vil", "ww", "bear", "hunter", "idiot"], [81, 71, 88, 31, 34, 40, 70, 94, 73, 79, 98, 48])

# Solution().canVillagersWin(["vil","ww","bear","hunter","ww","idiot","vil","vil","ww","vil","ww","vil"], [45,67,32,25,1,27,99,85,3,54,3,25])

# Solution().canVillagersWin(["bear", "vil", "vil", "ww", "vil", "vil", "idiot", "ww", "hunter", "ww", "ww", "vil"], [9, 55, 62, 74, 43, 70, 13, 23, 15, 78, 61, 66])
