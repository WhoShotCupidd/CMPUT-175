def bitonic50(a_list):
    if a_list[1] < a_list[2]:
        a_list[1], a_list[2] = a_list[2], a_list[1]
    if a_list[0] > a_list[2]:
        a_list[0], a_list[2] = a_list[2], a_list[0]
    if a_list[1] > a_list[2]:
        a_list[1], a_list[2] = a_list[2], a_list[1]
    if a_list[4] > a_list[5]:
        a_list[4], a_list[5] = a_list[5], a_list[4]
    if a_list[3] < a_list[5]:
        a_list[3], a_list[5] = a_list[5], a_list[3]
    if a_list[4] < a_list[5]:
        a_list[4], a_list[5] = a_list[5], a_list[4]
    if a_list[0] > a_list[4]:
        a_list[0], a_list[4] = a_list[4], a_list[0]
    if a_list[1] > a_list[5]:
        a_list[1], a_list[5] = a_list[5], a_list[1]
    if a_list[0] > a_list[1]:
        a_list[0], a_list[1] = a_list[1], a_list[0]
    if a_list[2] > a_list[4]:
        a_list[2], a_list[4] = a_list[4], a_list[2]
    if a_list[3] > a_list[5]:
        a_list[3], a_list[5] = a_list[5], a_list[3]
    if a_list[2] > a_list[3]:
        a_list[2], a_list[3] = a_list[3], a_list[2]
    if a_list[4] > a_list[5]:
        a_list[4], a_list[5] = a_list[5], a_list[4]
    if a_list[7] > a_list[8]:
        a_list[7], a_list[8] = a_list[8], a_list[7]
    if a_list[6] < a_list[8]:
        a_list[6], a_list[8] = a_list[8], a_list[6]
    if a_list[7] < a_list[8]:
        a_list[7], a_list[8] = a_list[8], a_list[7]
    if a_list[10] < a_list[11]:
        a_list[10], a_list[11] = a_list[11], a_list[10]
    if a_list[9] > a_list[11]:
        a_list[9], a_list[11] = a_list[11], a_list[9]
    if a_list[10] > a_list[11]:
        a_list[10], a_list[11] = a_list[11], a_list[10]
    if a_list[6] < a_list[10]:
        a_list[6], a_list[10] = a_list[10], a_list[6]
    if a_list[7] < a_list[11]:
        a_list[7], a_list[11] = a_list[11], a_list[7]
    if a_list[6] < a_list[7]:
        a_list[6], a_list[7] = a_list[7], a_list[6]
    if a_list[8] < a_list[10]:
        a_list[8], a_list[10] = a_list[10], a_list[8]
    if a_list[9] < a_list[11]:
        a_list[9], a_list[11] = a_list[11], a_list[9]
    if a_list[8] < a_list[9]:
        a_list[8], a_list[9] = a_list[9], a_list[8]
    if a_list[10] < a_list[11]:
        a_list[10], a_list[11] = a_list[11], a_list[10]
    if a_list[0] > a_list[8]:
        a_list[0], a_list[8] = a_list[8], a_list[0]
    if a_list[1] > a_list[9]:
        a_list[1], a_list[9] = a_list[9], a_list[1]
    if a_list[2] > a_list[10]:
        a_list[2], a_list[10] = a_list[10], a_list[2]
    if a_list[3] > a_list[11]:
        a_list[3], a_list[11] = a_list[11], a_list[3]
    if a_list[0] > a_list[2]:
        a_list[0], a_list[2] = a_list[2], a_list[0]
    if a_list[1] > a_list[3]:
        a_list[1], a_list[3] = a_list[3], a_list[1]
    if a_list[0] > a_list[1]:
        a_list[0], a_list[1] = a_list[1], a_list[0]
    if a_list[2] > a_list[3]:
        a_list[2], a_list[3] = a_list[3], a_list[2]
    if a_list[4] > a_list[8]:
        a_list[4], a_list[8] = a_list[8], a_list[4]
    if a_list[5] > a_list[9]:
        a_list[5], a_list[9] = a_list[9], a_list[5]
    if a_list[6] > a_list[10]:
        a_list[6], a_list[10] = a_list[10], a_list[6]
    if a_list[7] > a_list[11]:
        a_list[7], a_list[11] = a_list[11], a_list[7]
    if a_list[4] > a_list[6]:
        a_list[4], a_list[6] = a_list[6], a_list[4]
    if a_list[5] > a_list[7]:
        a_list[5], a_list[7] = a_list[7], a_list[5]
    if a_list[4] > a_list[5]:
        a_list[4], a_list[5] = a_list[5], a_list[4]
    if a_list[6] > a_list[7]:
        a_list[6], a_list[7] = a_list[7], a_list[6]
    if a_list[8] > a_list[10]:
        a_list[8], a_list[10] = a_list[10], a_list[8]
    if a_list[9] > a_list[11]:
        a_list[9], a_list[11] = a_list[11], a_list[9]
    if a_list[8] > a_list[9]:
        a_list[8], a_list[9] = a_list[9], a_list[8]
    if a_list[10] > a_list[11]:
        a_list[10], a_list[11] = a_list[11], a_list[10]
    if a_list[13] > a_list[14]:
        a_list[13], a_list[14] = a_list[14], a_list[13]
    if a_list[12] < a_list[14]:
        a_list[12], a_list[14] = a_list[14], a_list[12]
    if a_list[13] < a_list[14]:
        a_list[13], a_list[14] = a_list[14], a_list[13]
    if a_list[16] < a_list[17]:
        a_list[16], a_list[17] = a_list[17], a_list[16]
    if a_list[15] > a_list[17]:
        a_list[15], a_list[17] = a_list[17], a_list[15]
    if a_list[16] > a_list[17]:
        a_list[16], a_list[17] = a_list[17], a_list[16]
    if a_list[12] < a_list[16]:
        a_list[12], a_list[16] = a_list[16], a_list[12]
    if a_list[13] < a_list[17]:
        a_list[13], a_list[17] = a_list[17], a_list[13]
    if a_list[12] < a_list[13]:
        a_list[12], a_list[13] = a_list[13], a_list[12]
    if a_list[14] < a_list[16]:
        a_list[14], a_list[16] = a_list[16], a_list[14]
    if a_list[15] < a_list[17]:
        a_list[15], a_list[17] = a_list[17], a_list[15]
    if a_list[14] < a_list[15]:
        a_list[14], a_list[15] = a_list[15], a_list[14]
    if a_list[16] < a_list[17]:
        a_list[16], a_list[17] = a_list[17], a_list[16]
    if a_list[19] < a_list[20]:
        a_list[19], a_list[20] = a_list[20], a_list[19]
    if a_list[18] > a_list[20]:
        a_list[18], a_list[20] = a_list[20], a_list[18]
    if a_list[19] > a_list[20]:
        a_list[19], a_list[20] = a_list[20], a_list[19]
    if a_list[21] < a_list[22]:
        a_list[21], a_list[22] = a_list[22], a_list[21]
    if a_list[23] > a_list[24]:
        a_list[23], a_list[24] = a_list[24], a_list[23]
    if a_list[21] < a_list[23]:
        a_list[21], a_list[23] = a_list[23], a_list[21]
    if a_list[22] < a_list[24]:
        a_list[22], a_list[24] = a_list[24], a_list[22]
    if a_list[21] < a_list[22]:
        a_list[21], a_list[22] = a_list[22], a_list[21]
    if a_list[23] < a_list[24]:
        a_list[23], a_list[24] = a_list[24], a_list[23]
    if a_list[18] > a_list[22]:
        a_list[18], a_list[22] = a_list[22], a_list[18]
    if a_list[19] > a_list[23]:
        a_list[19], a_list[23] = a_list[23], a_list[19]
    if a_list[20] > a_list[24]:
        a_list[20], a_list[24] = a_list[24], a_list[20]
    if a_list[18] > a_list[20]:
        a_list[18], a_list[20] = a_list[20], a_list[18]
    if a_list[19] > a_list[20]:
        a_list[19], a_list[20] = a_list[20], a_list[19]
    if a_list[21] > a_list[23]:
        a_list[21], a_list[23] = a_list[23], a_list[21]
    if a_list[22] > a_list[24]:
        a_list[22], a_list[24] = a_list[24], a_list[22]
    if a_list[21] > a_list[22]:
        a_list[21], a_list[22] = a_list[22], a_list[21]
    if a_list[23] > a_list[24]:
        a_list[23], a_list[24] = a_list[24], a_list[23]
    if a_list[12] < a_list[20]:
        a_list[12], a_list[20] = a_list[20], a_list[12]
    if a_list[13] < a_list[21]:
        a_list[13], a_list[21] = a_list[21], a_list[13]
    if a_list[14] < a_list[22]:
        a_list[14], a_list[22] = a_list[22], a_list[14]
    if a_list[15] < a_list[23]:
        a_list[15], a_list[23] = a_list[23], a_list[15]
    if a_list[16] < a_list[24]:
        a_list[16], a_list[24] = a_list[24], a_list[16]
    if a_list[12] < a_list[16]:
        a_list[12], a_list[16] = a_list[16], a_list[12]
    if a_list[13] < a_list[15]:
        a_list[13], a_list[15] = a_list[15], a_list[13]
    if a_list[14] < a_list[16]:
        a_list[14], a_list[16] = a_list[16], a_list[14]
    if a_list[13] < a_list[14]:
        a_list[13], a_list[14] = a_list[14], a_list[13]
    if a_list[15] < a_list[16]:
        a_list[15], a_list[16] = a_list[16], a_list[15]
    if a_list[17] < a_list[21]:
        a_list[17], a_list[21] = a_list[21], a_list[17]
    if a_list[18] < a_list[22]:
        a_list[18], a_list[22] = a_list[22], a_list[18]
    if a_list[19] < a_list[23]:
        a_list[19], a_list[23] = a_list[23], a_list[19]
    if a_list[20] < a_list[24]:
        a_list[20], a_list[24] = a_list[24], a_list[20]
    if a_list[17] < a_list[19]:
        a_list[17], a_list[19] = a_list[19], a_list[17]
    if a_list[18] < a_list[20]:
        a_list[18], a_list[20] = a_list[20], a_list[18]
    if a_list[17] < a_list[18]:
        a_list[17], a_list[18] = a_list[18], a_list[17]
    if a_list[19] < a_list[20]:
        a_list[19], a_list[20] = a_list[20], a_list[19]
    if a_list[21] < a_list[23]:
        a_list[21], a_list[23] = a_list[23], a_list[21]
    if a_list[22] < a_list[24]:
        a_list[22], a_list[24] = a_list[24], a_list[22]
    if a_list[21] < a_list[22]:
        a_list[21], a_list[22] = a_list[22], a_list[21]
    if a_list[23] < a_list[24]:
        a_list[23], a_list[24] = a_list[24], a_list[23]
    if a_list[0] > a_list[16]:
        a_list[0], a_list[16] = a_list[16], a_list[0]
    if a_list[1] > a_list[17]:
        a_list[1], a_list[17] = a_list[17], a_list[1]
    if a_list[2] > a_list[18]:
        a_list[2], a_list[18] = a_list[18], a_list[2]
    if a_list[3] > a_list[19]:
        a_list[3], a_list[19] = a_list[19], a_list[3]
    if a_list[4] > a_list[20]:
        a_list[4], a_list[20] = a_list[20], a_list[4]
    if a_list[5] > a_list[21]:
        a_list[5], a_list[21] = a_list[21], a_list[5]
    if a_list[6] > a_list[22]:
        a_list[6], a_list[22] = a_list[22], a_list[6]
    if a_list[7] > a_list[23]:
        a_list[7], a_list[23] = a_list[23], a_list[7]
    if a_list[8] > a_list[24]:
        a_list[8], a_list[24] = a_list[24], a_list[8]
    if a_list[0] > a_list[8]:
        a_list[0], a_list[8] = a_list[8], a_list[0]
    if a_list[1] > a_list[5]:
        a_list[1], a_list[5] = a_list[5], a_list[1]
    if a_list[2] > a_list[6]:
        a_list[2], a_list[6] = a_list[6], a_list[2]
    if a_list[3] > a_list[7]:
        a_list[3], a_list[7] = a_list[7], a_list[3]
    if a_list[4] > a_list[8]:
        a_list[4], a_list[8] = a_list[8], a_list[4]
    if a_list[1] > a_list[3]:
        a_list[1], a_list[3] = a_list[3], a_list[1]
    if a_list[2] > a_list[4]:
        a_list[2], a_list[4] = a_list[4], a_list[2]
    if a_list[1] > a_list[2]:
        a_list[1], a_list[2] = a_list[2], a_list[1]
    if a_list[3] > a_list[4]:
        a_list[3], a_list[4] = a_list[4], a_list[3]
    if a_list[5] > a_list[7]:
        a_list[5], a_list[7] = a_list[7], a_list[5]
    if a_list[6] > a_list[8]:
        a_list[6], a_list[8] = a_list[8], a_list[6]
    if a_list[5] > a_list[6]:
        a_list[5], a_list[6] = a_list[6], a_list[5]
    if a_list[7] > a_list[8]:
        a_list[7], a_list[8] = a_list[8], a_list[7]
    if a_list[9] > a_list[17]:
        a_list[9], a_list[17] = a_list[17], a_list[9]
    if a_list[10] > a_list[18]:
        a_list[10], a_list[18] = a_list[18], a_list[10]
    if a_list[11] > a_list[19]:
        a_list[11], a_list[19] = a_list[19], a_list[11]
    if a_list[12] > a_list[20]:
        a_list[12], a_list[20] = a_list[20], a_list[12]
    if a_list[13] > a_list[21]:
        a_list[13], a_list[21] = a_list[21], a_list[13]
    if a_list[14] > a_list[22]:
        a_list[14], a_list[22] = a_list[22], a_list[14]
    if a_list[15] > a_list[23]:
        a_list[15], a_list[23] = a_list[23], a_list[15]
    if a_list[16] > a_list[24]:
        a_list[16], a_list[24] = a_list[24], a_list[16]
    if a_list[9] > a_list[13]:
        a_list[9], a_list[13] = a_list[13], a_list[9]
    if a_list[10] > a_list[14]:
        a_list[10], a_list[14] = a_list[14], a_list[10]
    if a_list[11] > a_list[15]:
        a_list[11], a_list[15] = a_list[15], a_list[11]
    if a_list[12] > a_list[16]:
        a_list[12], a_list[16] = a_list[16], a_list[12]
    if a_list[9] > a_list[11]:
        a_list[9], a_list[11] = a_list[11], a_list[9]
    if a_list[10] > a_list[12]:
        a_list[10], a_list[12] = a_list[12], a_list[10]
    if a_list[9] > a_list[10]:
        a_list[9], a_list[10] = a_list[10], a_list[9]
    if a_list[11] > a_list[12]:
        a_list[11], a_list[12] = a_list[12], a_list[11]
    if a_list[13] > a_list[15]:
        a_list[13], a_list[15] = a_list[15], a_list[13]
    if a_list[14] > a_list[16]:
        a_list[14], a_list[16] = a_list[16], a_list[14]
    if a_list[13] > a_list[14]:
        a_list[13], a_list[14] = a_list[14], a_list[13]
    if a_list[15] > a_list[16]:
        a_list[15], a_list[16] = a_list[16], a_list[15]
    if a_list[17] > a_list[21]:
        a_list[17], a_list[21] = a_list[21], a_list[17]
    if a_list[18] > a_list[22]:
        a_list[18], a_list[22] = a_list[22], a_list[18]
    if a_list[19] > a_list[23]:
        a_list[19], a_list[23] = a_list[23], a_list[19]
    if a_list[20] > a_list[24]:
        a_list[20], a_list[24] = a_list[24], a_list[20]
    if a_list[17] > a_list[19]:
        a_list[17], a_list[19] = a_list[19], a_list[17]
    if a_list[18] > a_list[20]:
        a_list[18], a_list[20] = a_list[20], a_list[18]
    if a_list[17] > a_list[18]:
        a_list[17], a_list[18] = a_list[18], a_list[17]
    if a_list[19] > a_list[20]:
        a_list[19], a_list[20] = a_list[20], a_list[19]
    if a_list[21] > a_list[23]:
        a_list[21], a_list[23] = a_list[23], a_list[21]
    if a_list[22] > a_list[24]:
        a_list[22], a_list[24] = a_list[24], a_list[22]
    if a_list[21] > a_list[22]:
        a_list[21], a_list[22] = a_list[22], a_list[21]
    if a_list[23] > a_list[24]:
        a_list[23], a_list[24] = a_list[24], a_list[23]
    if a_list[26] > a_list[27]:
        a_list[26], a_list[27] = a_list[27], a_list[26]
    if a_list[25] < a_list[27]:
        a_list[25], a_list[27] = a_list[27], a_list[25]
    if a_list[26] < a_list[27]:
        a_list[26], a_list[27] = a_list[27], a_list[26]
    if a_list[29] < a_list[30]:
        a_list[29], a_list[30] = a_list[30], a_list[29]
    if a_list[28] > a_list[30]:
        a_list[28], a_list[30] = a_list[30], a_list[28]
    if a_list[29] > a_list[30]:
        a_list[29], a_list[30] = a_list[30], a_list[29]
    if a_list[25] < a_list[29]:
        a_list[25], a_list[29] = a_list[29], a_list[25]
    if a_list[26] < a_list[30]:
        a_list[26], a_list[30] = a_list[30], a_list[26]
    if a_list[25] < a_list[26]:
        a_list[25], a_list[26] = a_list[26], a_list[25]
    if a_list[27] < a_list[29]:
        a_list[27], a_list[29] = a_list[29], a_list[27]
    if a_list[28] < a_list[30]:
        a_list[28], a_list[30] = a_list[30], a_list[28]
    if a_list[27] < a_list[28]:
        a_list[27], a_list[28] = a_list[28], a_list[27]
    if a_list[29] < a_list[30]:
        a_list[29], a_list[30] = a_list[30], a_list[29]
    if a_list[32] < a_list[33]:
        a_list[32], a_list[33] = a_list[33], a_list[32]
    if a_list[31] > a_list[33]:
        a_list[31], a_list[33] = a_list[33], a_list[31]
    if a_list[32] > a_list[33]:
        a_list[32], a_list[33] = a_list[33], a_list[32]
    if a_list[35] > a_list[36]:
        a_list[35], a_list[36] = a_list[36], a_list[35]
    if a_list[34] < a_list[36]:
        a_list[34], a_list[36] = a_list[36], a_list[34]
    if a_list[35] < a_list[36]:
        a_list[35], a_list[36] = a_list[36], a_list[35]
    if a_list[31] > a_list[35]:
        a_list[31], a_list[35] = a_list[35], a_list[31]
    if a_list[32] > a_list[36]:
        a_list[32], a_list[36] = a_list[36], a_list[32]
    if a_list[31] > a_list[32]:
        a_list[31], a_list[32] = a_list[32], a_list[31]
    if a_list[33] > a_list[35]:
        a_list[33], a_list[35] = a_list[35], a_list[33]
    if a_list[34] > a_list[36]:
        a_list[34], a_list[36] = a_list[36], a_list[34]
    if a_list[33] > a_list[34]:
        a_list[33], a_list[34] = a_list[34], a_list[33]
    if a_list[35] > a_list[36]:
        a_list[35], a_list[36] = a_list[36], a_list[35]
    if a_list[25] < a_list[33]:
        a_list[25], a_list[33] = a_list[33], a_list[25]
    if a_list[26] < a_list[34]:
        a_list[26], a_list[34] = a_list[34], a_list[26]
    if a_list[27] < a_list[35]:
        a_list[27], a_list[35] = a_list[35], a_list[27]
    if a_list[28] < a_list[36]:
        a_list[28], a_list[36] = a_list[36], a_list[28]
    if a_list[25] < a_list[27]:
        a_list[25], a_list[27] = a_list[27], a_list[25]
    if a_list[26] < a_list[28]:
        a_list[26], a_list[28] = a_list[28], a_list[26]
    if a_list[25] < a_list[26]:
        a_list[25], a_list[26] = a_list[26], a_list[25]
    if a_list[27] < a_list[28]:
        a_list[27], a_list[28] = a_list[28], a_list[27]
    if a_list[29] < a_list[33]:
        a_list[29], a_list[33] = a_list[33], a_list[29]
    if a_list[30] < a_list[34]:
        a_list[30], a_list[34] = a_list[34], a_list[30]
    if a_list[31] < a_list[35]:
        a_list[31], a_list[35] = a_list[35], a_list[31]
    if a_list[32] < a_list[36]:
        a_list[32], a_list[36] = a_list[36], a_list[32]
    if a_list[29] < a_list[31]:
        a_list[29], a_list[31] = a_list[31], a_list[29]
    if a_list[30] < a_list[32]:
        a_list[30], a_list[32] = a_list[32], a_list[30]
    if a_list[29] < a_list[30]:
        a_list[29], a_list[30] = a_list[30], a_list[29]
    if a_list[31] < a_list[32]:
        a_list[31], a_list[32] = a_list[32], a_list[31]
    if a_list[33] < a_list[35]:
        a_list[33], a_list[35] = a_list[35], a_list[33]
    if a_list[34] < a_list[36]:
        a_list[34], a_list[36] = a_list[36], a_list[34]
    if a_list[33] < a_list[34]:
        a_list[33], a_list[34] = a_list[34], a_list[33]
    if a_list[35] < a_list[36]:
        a_list[35], a_list[36] = a_list[36], a_list[35]
    if a_list[38] < a_list[39]:
        a_list[38], a_list[39] = a_list[39], a_list[38]
    if a_list[37] > a_list[39]:
        a_list[37], a_list[39] = a_list[39], a_list[37]
    if a_list[38] > a_list[39]:
        a_list[38], a_list[39] = a_list[39], a_list[38]
    if a_list[41] > a_list[42]:
        a_list[41], a_list[42] = a_list[42], a_list[41]
    if a_list[40] < a_list[42]:
        a_list[40], a_list[42] = a_list[42], a_list[40]
    if a_list[41] < a_list[42]:
        a_list[41], a_list[42] = a_list[42], a_list[41]
    if a_list[37] > a_list[41]:
        a_list[37], a_list[41] = a_list[41], a_list[37]
    if a_list[38] > a_list[42]:
        a_list[38], a_list[42] = a_list[42], a_list[38]
    if a_list[37] > a_list[38]:
        a_list[37], a_list[38] = a_list[38], a_list[37]
    if a_list[39] > a_list[41]:
        a_list[39], a_list[41] = a_list[41], a_list[39]
    if a_list[40] > a_list[42]:
        a_list[40], a_list[42] = a_list[42], a_list[40]
    if a_list[39] > a_list[40]:
        a_list[39], a_list[40] = a_list[40], a_list[39]
    if a_list[41] > a_list[42]:
        a_list[41], a_list[42] = a_list[42], a_list[41]
    if a_list[44] > a_list[45]:
        a_list[44], a_list[45] = a_list[45], a_list[44]
    if a_list[43] < a_list[45]:
        a_list[43], a_list[45] = a_list[45], a_list[43]
    if a_list[44] < a_list[45]:
        a_list[44], a_list[45] = a_list[45], a_list[44]
    if a_list[46] > a_list[47]:
        a_list[46], a_list[47] = a_list[47], a_list[46]
    if a_list[48] < a_list[49]:
        a_list[48], a_list[49] = a_list[49], a_list[48]
    if a_list[46] > a_list[48]:
        a_list[46], a_list[48] = a_list[48], a_list[46]
    if a_list[47] > a_list[49]:
        a_list[47], a_list[49] = a_list[49], a_list[47]
    if a_list[46] > a_list[47]:
        a_list[46], a_list[47] = a_list[47], a_list[46]
    if a_list[48] > a_list[49]:
        a_list[48], a_list[49] = a_list[49], a_list[48]
    if a_list[43] < a_list[47]:
        a_list[43], a_list[47] = a_list[47], a_list[43]
    if a_list[44] < a_list[48]:
        a_list[44], a_list[48] = a_list[48], a_list[44]
    if a_list[45] < a_list[49]:
        a_list[45], a_list[49] = a_list[49], a_list[45]
    if a_list[43] < a_list[45]:
        a_list[43], a_list[45] = a_list[45], a_list[43]
    if a_list[44] < a_list[45]:
        a_list[44], a_list[45] = a_list[45], a_list[44]
    if a_list[46] < a_list[48]:
        a_list[46], a_list[48] = a_list[48], a_list[46]
    if a_list[47] < a_list[49]:
        a_list[47], a_list[49] = a_list[49], a_list[47]
    if a_list[46] < a_list[47]:
        a_list[46], a_list[47] = a_list[47], a_list[46]
    if a_list[48] < a_list[49]:
        a_list[48], a_list[49] = a_list[49], a_list[48]
    if a_list[37] > a_list[45]:
        a_list[37], a_list[45] = a_list[45], a_list[37]
    if a_list[38] > a_list[46]:
        a_list[38], a_list[46] = a_list[46], a_list[38]
    if a_list[39] > a_list[47]:
        a_list[39], a_list[47] = a_list[47], a_list[39]
    if a_list[40] > a_list[48]:
        a_list[40], a_list[48] = a_list[48], a_list[40]
    if a_list[41] > a_list[49]:
        a_list[41], a_list[49] = a_list[49], a_list[41]
    if a_list[37] > a_list[41]:
        a_list[37], a_list[41] = a_list[41], a_list[37]
    if a_list[38] > a_list[40]:
        a_list[38], a_list[40] = a_list[40], a_list[38]
    if a_list[39] > a_list[41]:
        a_list[39], a_list[41] = a_list[41], a_list[39]
    if a_list[38] > a_list[39]:
        a_list[38], a_list[39] = a_list[39], a_list[38]
    if a_list[40] > a_list[41]:
        a_list[40], a_list[41] = a_list[41], a_list[40]
    if a_list[42] > a_list[46]:
        a_list[42], a_list[46] = a_list[46], a_list[42]
    if a_list[43] > a_list[47]:
        a_list[43], a_list[47] = a_list[47], a_list[43]
    if a_list[44] > a_list[48]:
        a_list[44], a_list[48] = a_list[48], a_list[44]
    if a_list[45] > a_list[49]:
        a_list[45], a_list[49] = a_list[49], a_list[45]
    if a_list[42] > a_list[44]:
        a_list[42], a_list[44] = a_list[44], a_list[42]
    if a_list[43] > a_list[45]:
        a_list[43], a_list[45] = a_list[45], a_list[43]
    if a_list[42] > a_list[43]:
        a_list[42], a_list[43] = a_list[43], a_list[42]
    if a_list[44] > a_list[45]:
        a_list[44], a_list[45] = a_list[45], a_list[44]
    if a_list[46] > a_list[48]:
        a_list[46], a_list[48] = a_list[48], a_list[46]
    if a_list[47] > a_list[49]:
        a_list[47], a_list[49] = a_list[49], a_list[47]
    if a_list[46] > a_list[47]:
        a_list[46], a_list[47] = a_list[47], a_list[46]
    if a_list[48] > a_list[49]:
        a_list[48], a_list[49] = a_list[49], a_list[48]
    if a_list[25] < a_list[41]:
        a_list[25], a_list[41] = a_list[41], a_list[25]
    if a_list[26] < a_list[42]:
        a_list[26], a_list[42] = a_list[42], a_list[26]
    if a_list[27] < a_list[43]:
        a_list[27], a_list[43] = a_list[43], a_list[27]
    if a_list[28] < a_list[44]:
        a_list[28], a_list[44] = a_list[44], a_list[28]
    if a_list[29] < a_list[45]:
        a_list[29], a_list[45] = a_list[45], a_list[29]
    if a_list[30] < a_list[46]:
        a_list[30], a_list[46] = a_list[46], a_list[30]
    if a_list[31] < a_list[47]:
        a_list[31], a_list[47] = a_list[47], a_list[31]
    if a_list[32] < a_list[48]:
        a_list[32], a_list[48] = a_list[48], a_list[32]
    if a_list[33] < a_list[49]:
        a_list[33], a_list[49] = a_list[49], a_list[33]
    if a_list[25] < a_list[33]:
        a_list[25], a_list[33] = a_list[33], a_list[25]
    if a_list[26] < a_list[30]:
        a_list[26], a_list[30] = a_list[30], a_list[26]
    if a_list[27] < a_list[31]:
        a_list[27], a_list[31] = a_list[31], a_list[27]
    if a_list[28] < a_list[32]:
        a_list[28], a_list[32] = a_list[32], a_list[28]
    if a_list[29] < a_list[33]:
        a_list[29], a_list[33] = a_list[33], a_list[29]
    if a_list[26] < a_list[28]:
        a_list[26], a_list[28] = a_list[28], a_list[26]
    if a_list[27] < a_list[29]:
        a_list[27], a_list[29] = a_list[29], a_list[27]
    if a_list[26] < a_list[27]:
        a_list[26], a_list[27] = a_list[27], a_list[26]
    if a_list[28] < a_list[29]:
        a_list[28], a_list[29] = a_list[29], a_list[28]
    if a_list[30] < a_list[32]:
        a_list[30], a_list[32] = a_list[32], a_list[30]
    if a_list[31] < a_list[33]:
        a_list[31], a_list[33] = a_list[33], a_list[31]
    if a_list[30] < a_list[31]:
        a_list[30], a_list[31] = a_list[31], a_list[30]
    if a_list[32] < a_list[33]:
        a_list[32], a_list[33] = a_list[33], a_list[32]
    if a_list[34] < a_list[42]:
        a_list[34], a_list[42] = a_list[42], a_list[34]
    if a_list[35] < a_list[43]:
        a_list[35], a_list[43] = a_list[43], a_list[35]
    if a_list[36] < a_list[44]:
        a_list[36], a_list[44] = a_list[44], a_list[36]
    if a_list[37] < a_list[45]:
        a_list[37], a_list[45] = a_list[45], a_list[37]
    if a_list[38] < a_list[46]:
        a_list[38], a_list[46] = a_list[46], a_list[38]
    if a_list[39] < a_list[47]:
        a_list[39], a_list[47] = a_list[47], a_list[39]
    if a_list[40] < a_list[48]:
        a_list[40], a_list[48] = a_list[48], a_list[40]
    if a_list[41] < a_list[49]:
        a_list[41], a_list[49] = a_list[49], a_list[41]
    if a_list[34] < a_list[38]:
        a_list[34], a_list[38] = a_list[38], a_list[34]
    if a_list[35] < a_list[39]:
        a_list[35], a_list[39] = a_list[39], a_list[35]
    if a_list[36] < a_list[40]:
        a_list[36], a_list[40] = a_list[40], a_list[36]
    if a_list[37] < a_list[41]:
        a_list[37], a_list[41] = a_list[41], a_list[37]
    if a_list[34] < a_list[36]:
        a_list[34], a_list[36] = a_list[36], a_list[34]
    if a_list[35] < a_list[37]:
        a_list[35], a_list[37] = a_list[37], a_list[35]
    if a_list[34] < a_list[35]:
        a_list[34], a_list[35] = a_list[35], a_list[34]
    if a_list[36] < a_list[37]:
        a_list[36], a_list[37] = a_list[37], a_list[36]
    if a_list[38] < a_list[40]:
        a_list[38], a_list[40] = a_list[40], a_list[38]
    if a_list[39] < a_list[41]:
        a_list[39], a_list[41] = a_list[41], a_list[39]
    if a_list[38] < a_list[39]:
        a_list[38], a_list[39] = a_list[39], a_list[38]
    if a_list[40] < a_list[41]:
        a_list[40], a_list[41] = a_list[41], a_list[40]
    if a_list[42] < a_list[46]:
        a_list[42], a_list[46] = a_list[46], a_list[42]
    if a_list[43] < a_list[47]:
        a_list[43], a_list[47] = a_list[47], a_list[43]
    if a_list[44] < a_list[48]:
        a_list[44], a_list[48] = a_list[48], a_list[44]
    if a_list[45] < a_list[49]:
        a_list[45], a_list[49] = a_list[49], a_list[45]
    if a_list[42] < a_list[44]:
        a_list[42], a_list[44] = a_list[44], a_list[42]
    if a_list[43] < a_list[45]:
        a_list[43], a_list[45] = a_list[45], a_list[43]
    if a_list[42] < a_list[43]:
        a_list[42], a_list[43] = a_list[43], a_list[42]
    if a_list[44] < a_list[45]:
        a_list[44], a_list[45] = a_list[45], a_list[44]
    if a_list[46] < a_list[48]:
        a_list[46], a_list[48] = a_list[48], a_list[46]
    if a_list[47] < a_list[49]:
        a_list[47], a_list[49] = a_list[49], a_list[47]
    if a_list[46] < a_list[47]:
        a_list[46], a_list[47] = a_list[47], a_list[46]
    if a_list[48] < a_list[49]:
        a_list[48], a_list[49] = a_list[49], a_list[48]
    if a_list[0] > a_list[32]:
        a_list[0], a_list[32] = a_list[32], a_list[0]
    if a_list[1] > a_list[33]:
        a_list[1], a_list[33] = a_list[33], a_list[1]
    if a_list[2] > a_list[34]:
        a_list[2], a_list[34] = a_list[34], a_list[2]
    if a_list[3] > a_list[35]:
        a_list[3], a_list[35] = a_list[35], a_list[3]
    if a_list[4] > a_list[36]:
        a_list[4], a_list[36] = a_list[36], a_list[4]
    if a_list[5] > a_list[37]:
        a_list[5], a_list[37] = a_list[37], a_list[5]
    if a_list[6] > a_list[38]:
        a_list[6], a_list[38] = a_list[38], a_list[6]
    if a_list[7] > a_list[39]:
        a_list[7], a_list[39] = a_list[39], a_list[7]
    if a_list[8] > a_list[40]:
        a_list[8], a_list[40] = a_list[40], a_list[8]
    if a_list[9] > a_list[41]:
        a_list[9], a_list[41] = a_list[41], a_list[9]
    if a_list[10] > a_list[42]:
        a_list[10], a_list[42] = a_list[42], a_list[10]
    if a_list[11] > a_list[43]:
        a_list[11], a_list[43] = a_list[43], a_list[11]
    if a_list[12] > a_list[44]:
        a_list[12], a_list[44] = a_list[44], a_list[12]
    if a_list[13] > a_list[45]:
        a_list[13], a_list[45] = a_list[45], a_list[13]
    if a_list[14] > a_list[46]:
        a_list[14], a_list[46] = a_list[46], a_list[14]
    if a_list[15] > a_list[47]:
        a_list[15], a_list[47] = a_list[47], a_list[15]
    if a_list[16] > a_list[48]:
        a_list[16], a_list[48] = a_list[48], a_list[16]
    if a_list[17] > a_list[49]:
        a_list[17], a_list[49] = a_list[49], a_list[17]
    if a_list[0] > a_list[16]:
        a_list[0], a_list[16] = a_list[16], a_list[0]
    if a_list[1] > a_list[17]:
        a_list[1], a_list[17] = a_list[17], a_list[1]
    if a_list[0] > a_list[1]:
        a_list[0], a_list[1] = a_list[1], a_list[0]
    if a_list[2] > a_list[10]:
        a_list[2], a_list[10] = a_list[10], a_list[2]
    if a_list[3] > a_list[11]:
        a_list[3], a_list[11] = a_list[11], a_list[3]
    if a_list[4] > a_list[12]:
        a_list[4], a_list[12] = a_list[12], a_list[4]
    if a_list[5] > a_list[13]:
        a_list[5], a_list[13] = a_list[13], a_list[5]
    if a_list[6] > a_list[14]:
        a_list[6], a_list[14] = a_list[14], a_list[6]
    if a_list[7] > a_list[15]:
        a_list[7], a_list[15] = a_list[15], a_list[7]
    if a_list[8] > a_list[16]:
        a_list[8], a_list[16] = a_list[16], a_list[8]
    if a_list[9] > a_list[17]:
        a_list[9], a_list[17] = a_list[17], a_list[9]
    if a_list[2] > a_list[6]:
        a_list[2], a_list[6] = a_list[6], a_list[2]
    if a_list[3] > a_list[7]:
        a_list[3], a_list[7] = a_list[7], a_list[3]
    if a_list[4] > a_list[8]:
        a_list[4], a_list[8] = a_list[8], a_list[4]
    if a_list[5] > a_list[9]:
        a_list[5], a_list[9] = a_list[9], a_list[5]
    if a_list[2] > a_list[4]:
        a_list[2], a_list[4] = a_list[4], a_list[2]
    if a_list[3] > a_list[5]:
        a_list[3], a_list[5] = a_list[5], a_list[3]
    if a_list[2] > a_list[3]:
        a_list[2], a_list[3] = a_list[3], a_list[2]
    if a_list[4] > a_list[5]:
        a_list[4], a_list[5] = a_list[5], a_list[4]
    if a_list[6] > a_list[8]:
        a_list[6], a_list[8] = a_list[8], a_list[6]
    if a_list[7] > a_list[9]:
        a_list[7], a_list[9] = a_list[9], a_list[7]
    if a_list[6] > a_list[7]:
        a_list[6], a_list[7] = a_list[7], a_list[6]
    if a_list[8] > a_list[9]:
        a_list[8], a_list[9] = a_list[9], a_list[8]
    if a_list[10] > a_list[14]:
        a_list[10], a_list[14] = a_list[14], a_list[10]
    if a_list[11] > a_list[15]:
        a_list[11], a_list[15] = a_list[15], a_list[11]
    if a_list[12] > a_list[16]:
        a_list[12], a_list[16] = a_list[16], a_list[12]
    if a_list[13] > a_list[17]:
        a_list[13], a_list[17] = a_list[17], a_list[13]
    if a_list[10] > a_list[12]:
        a_list[10], a_list[12] = a_list[12], a_list[10]
    if a_list[11] > a_list[13]:
        a_list[11], a_list[13] = a_list[13], a_list[11]
    if a_list[10] > a_list[11]:
        a_list[10], a_list[11] = a_list[11], a_list[10]
    if a_list[12] > a_list[13]:
        a_list[12], a_list[13] = a_list[13], a_list[12]
    if a_list[14] > a_list[16]:
        a_list[14], a_list[16] = a_list[16], a_list[14]
    if a_list[15] > a_list[17]:
        a_list[15], a_list[17] = a_list[17], a_list[15]
    if a_list[14] > a_list[15]:
        a_list[14], a_list[15] = a_list[15], a_list[14]
    if a_list[16] > a_list[17]:
        a_list[16], a_list[17] = a_list[17], a_list[16]
    if a_list[18] > a_list[34]:
        a_list[18], a_list[34] = a_list[34], a_list[18]
    if a_list[19] > a_list[35]:
        a_list[19], a_list[35] = a_list[35], a_list[19]
    if a_list[20] > a_list[36]:
        a_list[20], a_list[36] = a_list[36], a_list[20]
    if a_list[21] > a_list[37]:
        a_list[21], a_list[37] = a_list[37], a_list[21]
    if a_list[22] > a_list[38]:
        a_list[22], a_list[38] = a_list[38], a_list[22]
    if a_list[23] > a_list[39]:
        a_list[23], a_list[39] = a_list[39], a_list[23]
    if a_list[24] > a_list[40]:
        a_list[24], a_list[40] = a_list[40], a_list[24]
    if a_list[25] > a_list[41]:
        a_list[25], a_list[41] = a_list[41], a_list[25]
    if a_list[26] > a_list[42]:
        a_list[26], a_list[42] = a_list[42], a_list[26]
    if a_list[27] > a_list[43]:
        a_list[27], a_list[43] = a_list[43], a_list[27]
    if a_list[28] > a_list[44]:
        a_list[28], a_list[44] = a_list[44], a_list[28]
    if a_list[29] > a_list[45]:
        a_list[29], a_list[45] = a_list[45], a_list[29]
    if a_list[30] > a_list[46]:
        a_list[30], a_list[46] = a_list[46], a_list[30]
    if a_list[31] > a_list[47]:
        a_list[31], a_list[47] = a_list[47], a_list[31]
    if a_list[32] > a_list[48]:
        a_list[32], a_list[48] = a_list[48], a_list[32]
    if a_list[33] > a_list[49]:
        a_list[33], a_list[49] = a_list[49], a_list[33]
    if a_list[18] > a_list[26]:
        a_list[18], a_list[26] = a_list[26], a_list[18]
    if a_list[19] > a_list[27]:
        a_list[19], a_list[27] = a_list[27], a_list[19]
    if a_list[20] > a_list[28]:
        a_list[20], a_list[28] = a_list[28], a_list[20]
    if a_list[21] > a_list[29]:
        a_list[21], a_list[29] = a_list[29], a_list[21]
    if a_list[22] > a_list[30]:
        a_list[22], a_list[30] = a_list[30], a_list[22]
    if a_list[23] > a_list[31]:
        a_list[23], a_list[31] = a_list[31], a_list[23]
    if a_list[24] > a_list[32]:
        a_list[24], a_list[32] = a_list[32], a_list[24]
    if a_list[25] > a_list[33]:
        a_list[25], a_list[33] = a_list[33], a_list[25]
    if a_list[18] > a_list[22]:
        a_list[18], a_list[22] = a_list[22], a_list[18]
    if a_list[19] > a_list[23]:
        a_list[19], a_list[23] = a_list[23], a_list[19]
    if a_list[20] > a_list[24]:
        a_list[20], a_list[24] = a_list[24], a_list[20]
    if a_list[21] > a_list[25]:
        a_list[21], a_list[25] = a_list[25], a_list[21]
    if a_list[18] > a_list[20]:
        a_list[18], a_list[20] = a_list[20], a_list[18]
    if a_list[19] > a_list[21]:
        a_list[19], a_list[21] = a_list[21], a_list[19]
    if a_list[18] > a_list[19]:
        a_list[18], a_list[19] = a_list[19], a_list[18]
    if a_list[20] > a_list[21]:
        a_list[20], a_list[21] = a_list[21], a_list[20]
    if a_list[22] > a_list[24]:
        a_list[22], a_list[24] = a_list[24], a_list[22]
    if a_list[23] > a_list[25]:
        a_list[23], a_list[25] = a_list[25], a_list[23]
    if a_list[22] > a_list[23]:
        a_list[22], a_list[23] = a_list[23], a_list[22]
    if a_list[24] > a_list[25]:
        a_list[24], a_list[25] = a_list[25], a_list[24]
    if a_list[26] > a_list[30]:
        a_list[26], a_list[30] = a_list[30], a_list[26]
    if a_list[27] > a_list[31]:
        a_list[27], a_list[31] = a_list[31], a_list[27]
    if a_list[28] > a_list[32]:
        a_list[28], a_list[32] = a_list[32], a_list[28]
    if a_list[29] > a_list[33]:
        a_list[29], a_list[33] = a_list[33], a_list[29]
    if a_list[26] > a_list[28]:
        a_list[26], a_list[28] = a_list[28], a_list[26]
    if a_list[27] > a_list[29]:
        a_list[27], a_list[29] = a_list[29], a_list[27]
    if a_list[26] > a_list[27]:
        a_list[26], a_list[27] = a_list[27], a_list[26]
    if a_list[28] > a_list[29]:
        a_list[28], a_list[29] = a_list[29], a_list[28]
    if a_list[30] > a_list[32]:
        a_list[30], a_list[32] = a_list[32], a_list[30]
    if a_list[31] > a_list[33]:
        a_list[31], a_list[33] = a_list[33], a_list[31]
    if a_list[30] > a_list[31]:
        a_list[30], a_list[31] = a_list[31], a_list[30]
    if a_list[32] > a_list[33]:
        a_list[32], a_list[33] = a_list[33], a_list[32]
    if a_list[34] > a_list[42]:
        a_list[34], a_list[42] = a_list[42], a_list[34]
    if a_list[35] > a_list[43]:
        a_list[35], a_list[43] = a_list[43], a_list[35]
    if a_list[36] > a_list[44]:
        a_list[36], a_list[44] = a_list[44], a_list[36]
    if a_list[37] > a_list[45]:
        a_list[37], a_list[45] = a_list[45], a_list[37]
    if a_list[38] > a_list[46]:
        a_list[38], a_list[46] = a_list[46], a_list[38]
    if a_list[39] > a_list[47]:
        a_list[39], a_list[47] = a_list[47], a_list[39]
    if a_list[40] > a_list[48]:
        a_list[40], a_list[48] = a_list[48], a_list[40]
    if a_list[41] > a_list[49]:
        a_list[41], a_list[49] = a_list[49], a_list[41]
    if a_list[34] > a_list[38]:
        a_list[34], a_list[38] = a_list[38], a_list[34]
    if a_list[35] > a_list[39]:
        a_list[35], a_list[39] = a_list[39], a_list[35]
    if a_list[36] > a_list[40]:
        a_list[36], a_list[40] = a_list[40], a_list[36]
    if a_list[37] > a_list[41]:
        a_list[37], a_list[41] = a_list[41], a_list[37]
    if a_list[34] > a_list[36]:
        a_list[34], a_list[36] = a_list[36], a_list[34]
    if a_list[35] > a_list[37]:
        a_list[35], a_list[37] = a_list[37], a_list[35]
    if a_list[34] > a_list[35]:
        a_list[34], a_list[35] = a_list[35], a_list[34]
    if a_list[36] > a_list[37]:
        a_list[36], a_list[37] = a_list[37], a_list[36]
    if a_list[38] > a_list[40]:
        a_list[38], a_list[40] = a_list[40], a_list[38]
    if a_list[39] > a_list[41]:
        a_list[39], a_list[41] = a_list[41], a_list[39]
    if a_list[38] > a_list[39]:
        a_list[38], a_list[39] = a_list[39], a_list[38]
    if a_list[40] > a_list[41]:
        a_list[40], a_list[41] = a_list[41], a_list[40]
    if a_list[42] > a_list[46]:
        a_list[42], a_list[46] = a_list[46], a_list[42]
    if a_list[43] > a_list[47]:
        a_list[43], a_list[47] = a_list[47], a_list[43]
    if a_list[44] > a_list[48]:
        a_list[44], a_list[48] = a_list[48], a_list[44]
    if a_list[45] > a_list[49]:
        a_list[45], a_list[49] = a_list[49], a_list[45]
    if a_list[42] > a_list[44]:
        a_list[42], a_list[44] = a_list[44], a_list[42]
    if a_list[43] > a_list[45]:
        a_list[43], a_list[45] = a_list[45], a_list[43]
    if a_list[42] > a_list[43]:
        a_list[42], a_list[43] = a_list[43], a_list[42]
    if a_list[44] > a_list[45]:
        a_list[44], a_list[45] = a_list[45], a_list[44]
    if a_list[46] > a_list[48]:
        a_list[46], a_list[48] = a_list[48], a_list[46]
    if a_list[47] > a_list[49]:
        a_list[47], a_list[49] = a_list[49], a_list[47]
    if a_list[46] > a_list[47]:
        a_list[46], a_list[47] = a_list[47], a_list[46]
    if a_list[48] > a_list[49]:
        a_list[48], a_list[49] = a_list[49], a_list[48]
    return a_list
