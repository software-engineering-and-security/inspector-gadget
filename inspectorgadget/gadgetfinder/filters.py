
def filterStrict(gadgets):
    badins = ["ret", "retf", "iretd", "iret", "call", "lcall", "syscall", "int3", "loop", "loope", "loopne", "jmp", "je", "jne", "jg", "jng", "jge", "jnge", "jl", "jnl", "jle", "jnle", "jb", "jbe", "ja", "jna", "jae", "jnae", "js", "jnp", "jo", "jno", "fist" "hlt", "int", "in", "out", "enter"]
    #regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    
    gg = []
    bg = []
    
    for g in gadgets:
        bad = 0
        for i in g.instructions:
            instr = i[0 : i.find(" ")]
            if instr in badins:
                bad += 1
            
        # Check if a gadget changes rsp too much
#         for p in g.postconditions:
#             if "put(rsp)" in p:
#                 for r in regs:
#                     if r in p:
#                         bad += 1
            
        if bad == 1:
            gg.append(g)
        else:
            bg.append(g)
            
    return gg, bg

def filterSemiStrict(gadgets):
    badins = ["ret", "retf", "syscall", "int3", "loop", "loopne", "loope", "jmp", "je", "jne", "jg", "jng", "jge", "jnge", "jl", "jnl", "jle", "jnle", "jb", "jbe", "ja", "jna", "jae", "jnae", "js", "jnp", "jo", "jno", "fist" "hlt", "int", "in", "out", "enter"]
    #regs = ["rax", "rbx", "rcx", "rdx", "rsi", "rdi", "rbp", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]
    
    gg = []
    
    for g in gadgets:
        bad = 0
        calls = 0
        for i in g.instructions:
            instr = i[0 : i.find(" ")]
            if instr in badins:
                bad += 1
            
            if "call" in instr:
                calls += 1
            
        # Check if a gadget changes rsp too much
#         for p in g.postconditions:
#             if "put(rsp)" in p:
#                 for r in regs:
#                     if r in p:
#                         bad += 1
            
        if bad == 1 & calls == 1:
            gg.append(g)

    return gg
    


