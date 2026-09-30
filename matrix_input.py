def input_matrix(row1, col1):

    if row1==1 and col1==1:
        p= int(input("enter a₁₁:"))
        matrix = [[p]]
        print(matrix)

    elif row1==1 and col1==2:
        q=int(input("enter a₁₁:"))
        r=int(input("enter a₁₂:"))
        matrix=[[q,r]]
        print(matrix)

    elif row1==1 and col1==3:
        s=int(input("enter a₁₁:"))
        t=int(input("enter a₁₂:"))
        u=int(input("enter a₁₃:"))
        matrix=[[s,t,u]]
        print(matrix)

    elif row1==2 and col1==1:
        s=int(input("enter a₁₁:"))
        t=int(input("enter a₂₁:"))
        matrix=[[s],[t]]
        print(*matrix,sep="\n")

    elif row1==3 and col1==1:
        s=int(input("enter a₁₁:"))
        t=int(input("enter a₂₁:"))
        u=int(input("enter a₃₁:"))
        matrix=[[s],[t],[u]]
        print(*matrix,sep="\n")

    elif row1==2 and col1==2:
        s=int(input("enter a₁₁:"))
        t=int(input("enter a₁₂:"))
        u=int(input("enter a₂₁:"))
        v=int(input("enter a₂₂:"))
        matrix=[
            [s,t],
            [u,v]          
        ]
        print(*matrix,sep="\n")

    elif row1==2 and col1==3:
        s=int(input("enter a₁₁:"))
        t=int(input("enter a₁₂:"))
        u=int(input("enter a₁₃:"))
        v=int(input("enter a₂₁:"))
        x=int(input("enter a₂₂:"))
        y=int(input("enter a₂₃:"))
        matrix=[
            [s,t,u],
            [v,x,y]
        ]
        print(*matrix,sep="\n")

    elif row1==3 and col1==2:
        s=int(input("enter a₁₁:"))
        t=int(input("enter a₁₂:"))
        u=int(input("enter a₂₁:"))
        v=int(input("enter a₂₂:"))
        x=int(input("enter a₃₁:"))
        y=int(input("enter a₃₂:"))
        matrix=[
            [s,t],
            [u,v],
            [x,y]
        ]
        print(*matrix,sep="\n")

    elif row1==3 and col1==3:
        s=int(input("enter a₁₁:"))
        t=int(input("enter a₁₂:"))
        a=int(input("enter a₁₃:"))
        u=int(input("enter a₂₁:"))
        v=int(input("enter a₂₂:"))
        b=int(input("enter a₂₃:"))
        x=int(input("enter a₃₁:"))
        y=int(input("enter a₃₂:"))
        c=int(input("enter a₃₃:"))
        matrix=[
            [s,t,a],
            [u,v,b],
            [x,y,c]
        ]
        print(*matrix,sep="\n")

    return matrix