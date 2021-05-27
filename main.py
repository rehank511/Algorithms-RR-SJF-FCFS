import sys


def fcfs(pid, runtime, arrivetime, num):

    print("FCFS\n")
    ptime = 0
    wtsum = 0
    runq = []
    wt = [0] * num
    et = [0] * num
    st = [0] * num
    wt[0] = 0

    at = arrivetime[:]
    at.sort()

    for x in at:
        runq.append(pid[arrivetime.index(x)])

    st[0] = at[0]
    et[0] = st[0] + runtime[pid.index(runq[0])]

    # print(runq)
    # print(runq)
    for i in range(1, num):
        temp = pid.index(runq[i])
        st[i] = et[i-1]
        et[i] = st[i] + runtime[temp]
        wt[i] = st[i] - at[i]

    # for i in range(1, num):
    #     st[i] = st[i-1] + runtime[i-1]
    # print(st)
    #
    # for i in range(num):
    #     et[i] = st[i] + runtime[i]
    # print(et)
    #
    # for i in range(1, num):
    #     wt[i] = et[i-1] - arrivetime[i]
    # print(wt)
    print("PID\t\tArrival Time\t\tStart Time\t\tEnd Time\t\tRun Time\t\tWait Time")
    for i in range(num):
        print(str(runq[i]) + "\t\t" + str(at[i]) + "\t\t\t" + str(st[i]) + "\t\t\t" + str(et[i]) + "\t\t\t" +
              str(runtime[pid.index(runq[i])]) + "\t\t\t" + str(wt[i]))

    for x in wt:
        wtsum = wtsum + x

    avg = float(wtsum/num)
    print("Average Wait Time: ", avg)
    print("\n")


def sjf(pid, runtime, arrivetime, num):
    print("SJF\n")
    ptime = 0
    wtsum = 0
    waitq = []
    runq = []
    rt = []
    wt = [0] * num
    et = [0] * num
    st = [0] * num

    st[0] = 0
    wt[0] = 0
    for x in range(num):
        if arrivetime[x] == 0:
            runq.append(pid[x])
            ptime = runtime[0]
            et[0] = runtime[0]

    while len(runq) < num:

        # print(ptime)
        for i in range(1, num):
            if arrivetime[i] <= ptime and pid[i] not in runq and pid[i] not in waitq:
                waitq.append(pid[i])
                rt.append(runtime[i])
            # else:
            #     ptime += 1
                # print(waitq)
        q1 = 100000
        cnt = 0
        for x in rt:
            if x < q1:
                q1 = x
                cnt += 1

        temp = pid.index(waitq[cnt-1])
        runq.append(waitq.pop(cnt-1))
        rt.remove(runtime[temp])
        ptime = ptime + runtime[temp]

    for i in range(1, num):
        temp = pid.index(runq[i])
        st[i] = et[i-1]
        et[i] = st[i] + runtime[temp]
        wt[i] = st[i] - arrivetime[temp]

    for x in wt:
        wtsum = wtsum + x

    avg = float(wtsum/num)
    # print(avg)
    # print(st)
    # print(et)
    # print(wt)
    print("PID\t\tArrival Time\t\tStart Time\t\tEnd Time\t\tRun Time\t\tWait Time")
    for i in range(num):
        print(str(runq[i]) + "\t\t" + str(arrivetime[pid.index(runq[i])]) + "\t\t\t" + str(st[i]) + "\t\t\t" + str(et[i]) + "\t\t\t" +
              str(runtime[pid.index(runq[i])]) + "\t\t\t" + str(wt[i]))

    print("Average Wait Time: ", avg)
    print("\n")


def roundrobin(pid, runtime, arrivetime, num, quantum):
    print("Round Robin")
    ptime = 0
    wtsum = 0
    waitq = []
    runq = []
    wt = []
    endtime = [0] * num
    starttime = [0] * num
    et = []
    st = []
    rt = runtime[:]
    at = arrivetime[:]
    at.sort()
    repeat = []
    repeat1 = []

    while 1:
        count = 0
        for i in range(num):
            if arrivetime[i] <= ptime:
                waitq.append(pid[i])
            if rt[i] > int(quantum):
                count = 1
                rt[i] = rt[i] - int(quantum)
                ptime += int(quantum)
                # print(ptime)
                runq.append(pid[i])
            else:
                if rt[i] != 0:
                    count = 1
                    rt[i] = 0
                    ptime += rt[i]
                    # print(ptime)
                    runq.append(pid[i])
        if count == 0:
            break
    # print(runq)
    rt = []

    st.append(at[0])

    if runtime[pid.index(runq[0])] > int(quantum):
        et.append(st[0] + int(quantum))
        rt.append(int(quantum))
        repeat.append(runq[0])
    else:
        et.append(st[0] + runtime[pid.index(runq[0])])
        rt.append(runtime[pid.index(runq[0])])

    for i in range(1, len(runq)):
        st.append(et[i - 1])
        # if rt[i] > quantum:
        if runtime[pid.index(runq[i])] > int(quantum):
            if runq[i] not in repeat:
                repeat.append(runq[i])
                repeat1.append(int(quantum))
                # print(repeat)
                rt.append(int(quantum))
            else:
                count = 0
                # print(repeat)
                for x in repeat:
                    if x == runq[i]:
                        count += 1
                # print(count)
                num1 = runtime[pid.index(runq[i])] - (count*int(quantum))
                # print(num1)
                num1 = num1 - int(quantum)
                # print(num)
                if num1 >= 0:
                    rt.append(int(quantum))
                    et.append(st[i] + int(quantum))
                else:
                    rt.append(runtime[pid.index(runq[i])] % int(quantum))
                    et.append(st[i] + (runtime[pid.index(runq[i])] % int(quantum)))
                repeat.append(runq[i])
                repeat1.append(et[i])

            # for j in range(len(runq)):
            #     # print(i, j, runq[i], runq[j])
            #     if i != j:
            #         if runq[i] == runq[j]:
            #             repeat.append(runq[i])
        else:
            # if len(repeat) > 0:
            #     print(runtime[pid.index(runq[i])] % quantum)
            #     rt.append(runtime[pid.index(runq[i])] % quantum)
            rt.append(runtime[pid.index(runq[i])])
            et.append(st[i] + runtime[pid.index(runq[i])])

    print("PID\t\tStart Time\t\tEnd Time\t\tRun Time")
    for i in range(len(runq)):
        print(
            str(runq[i]) + "\t\t\t" + str(st[i]) + "\t\t\t\t" + str(
                et[i]) + "\t\t\t\t" +
            str(rt[i]))
    print("\n")

    print("PID\t\tArrival Time\t\tStart Time\t\tEnd Time\t\tRun Time\t\tWait Time")

    for q in range(num):

        if pid[q] in repeat:
            for y in repeat:
                if y == pid[q]:
                    # print(et[0])
                    # print(int(runq.index(pid[q])))
                    et.reverse()
                    endtime[q] = et[runq.index(pid[q])]
                    et.reverse()

        else:
            endtime[q] = et[runq.index(pid[q])]
        starttime[q] = st[runq.index(pid[q])]

    for e in range(num):
        wtsum += (endtime[e] - arrivetime[e] - runtime[e])
        print(str(pid[e]) + "\t\t\t" + str(arrivetime[e]) + "\t\t" + str(starttime[e]) + "\t\t\t" +
              str(endtime[e]) + "\t\t\t" + str(runtime[e]) + "\t\t\t"
              + str(endtime[e] - arrivetime[e] - runtime[e]))

    avg = float(wtsum / num)
    print("Average Wait Time: ", avg)
    print("\n")


def main():
    pid = []
    arrivetime = []
    runtime = []
    # quantum = 4
    filename = sys.argv[1]
    f = open(filename, "r")
    num = f.readline()
    num = int(num)
    contents = f.readlines()
    for x in contents:
        y = x.split()
        pid.append(int(y[0]))
        arrivetime.append(int(y[1]))
        runtime.append(int(y[2]))

    if sys.argv[2] == "FCFS":
        fcfs(pid, runtime, arrivetime, num)
    elif sys.argv[2] == "SJF":
        sjf(pid, runtime, arrivetime, num)
    elif sys.argv[2] == "RR":
        quantum = input("Enter the time quantum value: ")
        roundrobin(pid, runtime, arrivetime, num, quantum)


if __name__ == "__main__":
    main()
