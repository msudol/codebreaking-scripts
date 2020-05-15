# using concepts from here:
# https://pypi.org/project/py-enigma/

from enigma.machine import EnigmaMachine

ciphertext = 'UXKSCQNBOHJTXITNEOUZTOGSKEYQOGMGXQUPICHZRS'

# setup machine according to specs from a daily key sheet:
machine = EnigmaMachine.from_key_sheet(
       rotors='II IV V',
       reflector='B',
       ring_settings='D H K',
       plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

# set machine initial starting position
machine.set_display('ZEI')

# decrypt the message key
msg_key = machine.process_text('UXK')

# decrypt the cipher text with the unencrypted message key
machine.set_display(msg_key)

# produce result
plaintext = machine.process_text(ciphertext)

print(plaintext)



