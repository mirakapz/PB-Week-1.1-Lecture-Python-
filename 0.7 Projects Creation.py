#0.7 Projects Creation
architectName = input()
projectCount = int(input())
HR_FOR_PROJ = 3

timeToFinish = projectCount * HR_FOR_PROJ

print(f"The architect {architectName} will need {timeToFinish} hours to complete {projectCount} project/s.")