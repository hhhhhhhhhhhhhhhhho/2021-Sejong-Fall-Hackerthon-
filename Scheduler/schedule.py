class Class:
    def __init__(self,name,id,id_divide,prof_name,tendency,day,start_time,end_time,term,class_hour,class_grade):
        self._class_name=name
        self._class_id=id
        self._class_id_divide=id_divide
        self._class_prof =prof_name
        self._class_tendency = tendency
        self._day= day
        self._start_time=start_time
        self._end_time=end_time
        self._term=term
        self._class_hour = class_hour
        self._class_grade = class_grade
        self._is_selected = False
        self._is_Inserted = False


    def Change_Start_time(target_class): # 30분 단위의 수업을 0.5 로 바꿔줍니다.
        hour = int(target_class._start_time[:2]) # 시간을 정수로 갖고 있습니다. 
        minute = int(target_class._start_time[4:]) # 분을 정수로 가져옵니다. 
        if minute == 30:
            minute = 0.5
        else:
            minute = 0
        return hour,minute

    def Change_End_time(target_class): # 30분 단위의 수업을 0.5 로 바꿔줍니다.
        hour = int(target_class._end_time[:2]) # 시간을 정수로 갖고 있습니다. 
        minute = int(target_class._end_time[4:]) # 분을 정수로 가져옵니다. 

        if minute == 30:
            minute = 0.5
        else:
            minute = 0

        return hour,minute

    def Change_day(target_class):
        if target_class._day == '월':
            return 0
        if target_class._day == '화':
            return 1
        if target_class._day == '수':
            return 2
        if target_class._day == '목':
            return 3
        if target_class._day == '금':
            return 4
        if target_class._day == '토':
            return 5
        if target_class._day == '일':
            return 6

    def Insert_class(self,schedule): #수업을 시간표에 집어넣는다.
        # shedule[self.starttime] = self
       
        start_hour,start_minute = Change_Start_time(self) 
        end_hour,end_minute=Change_End_time(self)

        #한 번 예약하는 경우에 그 날 운동하고 싶은 기구들을 모두 예약하는건가요 ? 아니면 당장 앞에 있는 가구만을 예약하는거나요 ?

        #5분 10분단위로 예약을 해야할텐데 자신의 루틴만 해결 하고 다른사람들은 고려하지 않는 루틴이 아닌가요 ?

        start_time = start_hour + start_minute # 13시 30분 인 경우 13.5로 바꿔줍니다.
        end_time = end_hour + end_minute# 13시 30분 인 경우 13.5로 바꿔줍니다.

        diff_time = end_time - start_time # 차이를 구합니다. 


        for i in range(start_hour,end_hour+1,2):
            #FIXME 시간넘어갈 수 있음, ㅋㅋ 산수는 어려웡 

            if i==start_hour:
                if start_minute == 0.5:
                    schedule[Change_day(self._day)][i+1] = self # 
                else:
                    schedule[Change_day(self._day)][i] = self #    

            if i==end_hour:
                if end_minute==0.5:
                    schedule[Change_day(self._day)][i] = self #   
                    schedule[Change_day(self._day)][i+1] = self # 
                else: 
                    schedule[Change_day(self._day)][i] = self #    
            else:
                schedule[Change_day(self._day)][i] = self #
                schedule[Change_day(self._day)][i+1] = self # 


    def Is_overapping(self,schedule): #수업이 현재 시간표와 겹치지 않는지 확인합니다.
        start_hour , start_minute = Change_Start_time(self)
        end_hour , end_minute = Change_End_time(self)
        overlap_count=0

        for i in range(start_hour,end_hour+1): #30분 단위로 어떤 수업이 있는지 출력 함. 
            if schedule[Change_day(self._day)][i]._class_name!='':
                overlap_count=overlap_count+1
                print(i*2,"시 해당 되는 수업은. ",schedule[Change_day(self._day)][i])
                if i%2!=0:
                    print(i*2,"시 30분 해당 되는 수업은. ",schedule[Change_day(self._day)][i])


        if overlap_count!=0:
            print("겹치는 수업이 존재합니다. 해당 시간에 수업을 집어 넣을 수 없습니다.")
            return False

        else:
            print("겹치는 수업이 없습니다. 해당 시간에 수업을 집어넣을 수 있습니다.")
            return True

            ## 1. 위에서 겹치는지 확인  
            ## 확인하려는수업끝나는시간 - 원래수업시작시간(모든수업조회) <= 0
            

            ## 2. 아래서 겹치는지 확인
            ## 확인하려는수업시작시간 - 원래수업끝나는시간(모든수업조회) <= 0


            ## 3. 시간이 완벽하게 겹치는지 확인
            ## 확인하려는수업시작시간 != 원래수업시작시간
            ## 확인하려는수업종료시간 != 원래수업종료시간


    def Recommend_class(student,tendency,schedule): #학생에게 필수로 들어야하는 수업과 겹치지 않는는 수업들을 성향에 맞춰 추천해줍니다.
        ## 1. 성향 받아온것들로 리스트업
        ## 2. 강의평 많은 순 ,강의 평점 높은 순으로 다시 리스트업
        ## 3. 위에서부터 is_overapping 함수쓰면서 안겹치는것들 리스트업
        ## 4. 겹치지 않는 것들 리스트1에넣고 최대학점까지 리스트에 넣음음.
        ## 5. 리스트에에 들어간것들은은 is_selected = True
        ## 5. 최대학점지나면 리스트에 그만 넣고 종료
        ## 6. 3개 시간표 만들어질 때 까지 4-5 반복
        ## 7. 3개 시간표 리턴
        
        input_hour = 0
        ##TODO 아래는 입력되어야 할 DB 함수이ㅏㄷ. 
        tendency = student.Get_tendency() # 학생의 성향을 가져온다. 
        necessary_class = student.Load_necessaray_class() #학생이 꼭 들어야하는 수업을 가져온다.

        for necessary in necessary_class: ### 무조건 들어야 하는 수업들을 시간표에 집어 넣는다. 
            necessary.Insert_class(schedule)
            necessary._is_Inserted = True
            input_hour = input_hour + necessary._class_hour

        class_tendnecy = get_class_about_tendency(tendency) # 성향에 따른 수업을 가져온다. 
        class_tendency =sorted(class_tendency, key=lambda x : x[2]) #2 는 특정 열이다, 특정 열 기준으로 정렬 한다. 여기서는 평점 기준으로 정렬해야 한다. 

        for class_tendency_sorted_grade in class_tendency:
            if input_hour >= student._maximum_hour:
                print(" 최대 학점에 도달했습니다.")
                break

            if class_tendency_sorted_grade.Isoverapping(schedule) == True: ## 듣고싶은 성향의 수업을 리스트업하고, 평점이 높은 순으로 정렬하여 겹치는지 확인하고 수업을 집어넣습니다. 
                class_tendency_sorted_grade.Insert_class(schedule)
                class_tendency_sorted_grade._is_Inserted = True


        return schedule # 추천되는 수업과 필수로 들어야하는 수업이 들어있는 시간표를 반환합니다. 

        #SQL 에서 수업 리스트 받아엄. 


class Student:
    def __init__(self):
        self._name='none'
        self._id_number='18011000'
        self._major='CE'
        self._term='8'
        self._maximum_hour = 20
        self._tendency = []

    def Load_student_info(self): #학생의 개인정보를 가져옵니다.
        print(" 함수가 정의되지 않았습니다. ")
    def Load_schedule(self): #해당학생의 시간표를 불러옵니다. 
        print(" 함수가 정의되지 않았습니다. ")
    def Load_necessary_class(self):# 해당학생의 시간표를 불러오기 위해서 해당 학생이 꼭 들어야하는 수업을 가져옵니다.
        print(" 함수가 정의되지 않았습니다. ")  
    def Get_tendency(self): #학생의성향을을 가져옵니다.
        print(" 함수가 정의되지 않았습니다. ")


def Init_schedule(self):
    schedule = Class.__init__()
    for i in range(0,8):
        for j in range(0,49): #30분 단위로 쪼개기 위해서 49개의 행을 만듭니다.
            schedule.append(Class.__init())
    
    return schedule 


def Make_schedule(): #시간표를 만듭니다.
    print(" 함수가 정의되지 않았습니다. ")

