import os
import sys
import platform
import time

def os_check():
    if platform.system() != 'Linux':
        print('This is Specifically for linux')
        sys.exit()



if __name__ == '__main__':
    #checking os
    os_check()

    while True:
        #opitons
        print('1. Create new container\n2. Access already create container\n3. Close the Container\n4. Exit Script')
        user_choice = input('Enter the no: ')

        if user_choice == '1':
            if os.getuid() != '0':
                print('[+] If you are part of Sudo group, Please provide the password or run as root!')
                sudo_pass = input('Enter Sudo password: ')
                
                try:
                    #installing required packages
                    print('Installing/Upgrading required packages')
                    time.sleep(2)
                    os.system(f'echo -n {sudo_pass} | sudo -S apt install ecryptfs-utils\n')

                    dir_name = input('Choose a Directory name: ')

                    #creating a directory
                    print(f'\n[+] Creating a directory at location ~/Desktop/{dir_name}')
                    os.system(f'mkdir ~/Desktop/{dir_name}')


                    #performing steps
                    os.system(f'sudo mount -t ecryptfs ~/Desktop/{dir_name} ~/Desktop/{dir_name} ')
                    print('Container Created, Close the container after use .')
                    time.sleep(2)
                except:
                    print('Terminating encountered error!')
                    sys.exit()

            if os.getuid() == '0':
                try:
                    #installing required packages
                    os.system('apt install ecryptfs-utils')

                    dir_name = input('Choose a Directory name: ')

                    #creating a directory
                    print(f'\n[+] Creating a directory at location ~/Desktop/{dir_name}')
                    os.system(f'mkdir ~/Desktop/{dir_name}')


                    #performing steps
                    os.system(f'mount -t encryptfs ~/Desktop/{dir_name} ~/Desktop/{dir_name} ')
                    print('Container Created, Close the container after use.')
                    time.sleep(2)
                except:
                    print('Terminating encountered error!')
                    sys.exit()


        elif user_choice == '2':
            dir_name = input('Enter the name of container you want to access: ')

            if os.getuid() != '0':
                print('\n[+] If you are part of Sudo group, Please provide the password or run as root!\n')
                sudo_pass = input('Enter Sudo password: ')

                try:
                    os.system(f'echo -n {sudo_pass} | sudo -s -S')
                    os.system(f'sudo mount -t ecryptfs ~/Desktop/{dir_name} ~/Desktop/{dir_name}')

                    print('if above steps are done correct you can access the container now')
                    time.sleep(2)
                except:
                    print('Terminating some error Occurred')
                    sys.exit()
            if os.getuid() == '0':
                try:
                    #installing required packages
                    os.system(f'sudo  mount -t ecryptfs ~/Desktop/{dir_name} ~/Desktop/{dir_name}')
                    print('if above steps are done correct you can access the container now \n')
                    time.sleep(2)
                except:
                    print('Terminating some error Occurred')
                    sys.exit()


        elif user_choice == '3':
            dir_name = input('Name of the directory/Container you want to Close: ')
            if os.getuid() != '0':
                print('[+] If you are part of Sudo group, Please provide the password or run as root!')
                sudo_pass = input('Enter Sudo password: ')

                #unmounting the container
                os.system(f'echo -n {sudo_pass}| sudo -S umount ~/Desktop/{dir_name}')
                print('Done!')
                time.sleep(2)
            if os.getuid() == '0':
                os.system(f'sudo -S umount ~/Desktop/{dir_name}')
                print('Done!')
                time.sleep(2)



        elif user_choice == '4':
            sys.exit()
        else:
            continue
            

    