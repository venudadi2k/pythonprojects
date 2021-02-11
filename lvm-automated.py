from os import system as s

def setcolor(x) :
    s("tput setaf {}".format(x))

def waitforuser() :
    input("\n Press Enter key to continue\n")

def thankyou() :
    s("sleep 3")
    setcolor(3)
    print("\n\n THANK YOU FOR USING LVM AUTOMATER  !!")
    setcolor(7)


def createlvm() :

    print(" Create an LVM \n")
    print(" Attach external hard drives if any\n")
    waitforuser()
    print("\n Here is the list of all the avalilable harddisks \n")
    s("fdisk -l ")


    pvnames = input("\n Enter pv name/s to create pv : ")
    s("pvcreate {}".format(pvnames))

    waitforuser()
    print(" Here is list of PV's created\n")
    s("pvdisplay -C")

    vgname = input("\n Enter VG ( volume group ) name to create VG \n Example vg_name pv1 pv2 \n")
    s("vgcreate {}".format(vgname))

    waitforuser()
    print(" Here is list of VG's created\n")
    s("vgdisplay -C")

    lvname = input("\n Enter lv name to create lvm :")
    size = input(" Enter size of lvm to create : ")
    vgname = input(" Enter VG name to create lvm from the VG : ")
    s("lvcreate -n {} --size {} {}".format(lvname,size,vgname))

    waitforuser()
    print(" Here is list of LV's created\n")
    s("lvdisplay -C")

    print("\n Do you want to format the current lvm or pre existing lvm's if yes press \"y\" to continue else press \"e\" to exit : ")
    user_choice = input()

    if user_choice == "y":
        lvm_to_format = input("\n Enter lvm name to format , Example : /dev/myvg1/mylvm1 : ")
        s("mkfs.ext4 {}".format(lvm_to_format))
    else :
        pass

def resizelvm() :
    print(" Resize a LVM \n")
    lvm_to_resize =  input(" Enter the lvm name to resize : ")
    size = input(" Enter the size , For exapmle if you want to increase the size of 1 GB input +1G or to decrease the size of 1GB input -1G : ")
    s("lvresize --size {} {}".format(size,lvm_to_resize))
    print("\n")
    s("lvdisplay -C")
    print("\n")

def menu() :
    
    print(" Hey user , what do you want to do \n\n 1. Create LVM \n 2. Resize LVM\n 3. Exit LVM automator \n")
    choice = input(" Enter your choice : ")
    if choice == '1' :
        createlvm()
    elif choice == '2' :
        resizelvm()
    elif choice == '3' :
        exit()
        thankyou()
    else :
        print(" Invalid choice ")

# run the menu function till the user press 3 

setcolor(3)
print(" Welcome to LVM automator \n ")
setcolor(7)

while(1) :
    menu()
