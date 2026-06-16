class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
                #need int((target - position) / speed) + 1 miles to target 
        #once two cars in the same position, pop one off
        zipped = list(zip(position, speed))
        zipped.sort(key=lambda x:x[0])
        print(zipped)
        # now have zipped sorted
        fleet = 0
        leadpos, leadspeed = zipped.pop()
        #leadtimeneeded = (target - leadpos) / leadspeed
        while zipped:
            pos, speed = zipped.pop()
            if speed <= leadspeed:
                fleet += 1 # lead car is a fleet
                leadpos, leadspeed = pos, speed
            else:
                timeneeded = (leadpos - pos) / (speed-leadspeed)
                distancemet = timeneeded*(speed) + pos #if catch up to lead before lead at target
                if distancemet > target:
                    fleet +=1
                    leadpos, leadspeed = pos, speed

                #else:
                    #leadpos, leadspeed = distancemet, leadspeed
                

        return fleet+1