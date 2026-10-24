---
tipo: reuso
tags: [reuso, receitas]
---
# Receitas de treino extraídas dos artigos

Trechos detectados automaticamente nos PDFs (primeira ocorrência de cada item). **Confirme sempre no chunk indicado**; valores podem pertencer a um baseline e não ao modelo proposto.

| Artigo | Taxa de aprendizado | Batch | Épocas | Otimizador | Perda | Patch | Chunk |
|---|---|---|---|---|---|---|---|
| [[P01 Wagner 2023\|P01]] | `learning rate of 0.0001 was used` | `batch size of 256 images and the m` | `20000 epochs` |  | `binary cross-entropy and Dice coef` | `256 × 256 pixel` | [[P01 chunks#^P01_c017\|c017]] |
| [[P03 Carter 2024\|P03]] | `learning rate of 0.0001` | `batch size of 256 images and the m` | `25,000 epochs` | `Adam optimizer with a learning rat` | `binary cross-entropy and Dice coef` | `256 × 256 pixel` | [[P03 chunks#^P03_c016\|c016]] |
| [[P04 Wang 2024\|P04]] | `learning rate of 0.0001` |  | `50 epochs` | `Adam optimizer with a learning rat` | `Dice loss, which is a widely used ` |  | [[P04 chunks#^P04_c013\|c013]] |
| [[P09 Gonzalez-Velez 2026\|P09]] | `learning rate of 1.58 × 10−4 that ` | `batch size of 10 images, using the` | `300 epochs` | `AdamW optimizer with a weight deca` |  | `288 × 288 pixel` | [[P09 chunks#^P09_c027\|c027]] |
| [[P10 Etten 2021\|P10]] | `learning rate of 10−4 (baseline) o` |  | `300 epochs` | `Adam optimizer on the 1424 images ` | `BCE, where J is Jaccard distance a` | `1024 × 1024 pixel` | [[P10 chunks#^P10_c025\|c025]] |
| [[P12 Toker 2022\|P12]] |  |  |  |  |  | `1024x1024 with a pixel` | [[P12 chunks#^P12_c017\|c017]] |
| [[P13 Vincent 2024\|P13]] | `learning rate starting from 0 and ` |  |  | `AdamW optimizer [28] with a learni` | `focal loss [25] and the AdamW opti` |  | [[P13 chunks#^P13_c017\|c017]] |
| [[P15 Garnot 2021\|P15]] |  |  |  |  | `cross-entropy loss, and the size p` |  | [[P15 chunks#^P15_c021\|c021]] |
| [[P17 Metzger 2023\|P17]] | `learning rate of 10−4 ` | `batch size of 16, except for the l` |  | `Adam optimizer (Kingma and Ba 2014` | `binary cross-entropy loss` | `224×224 pixel` | [[P17 chunks#^P17_c013\|c013]] |
| [[P18 Daudt 2019\|P18]] |  |  |  |  |  | `631x602 pixel` | [[P18 chunks#^P18_c046\|c046]] |
| [[P19 Yang 2021\|P19]] | `learning rate is set as 0.005 and ` |  | `50 epochs` |  |  | `512 × 512 and is annotated at the ` | [[P19 chunks#^P19_c033\|c033]] |
| [[P21 Ding 2022\|P21]] |  | `batch size (8), running epochs (50` | `100 epochs` | `SGD) with Nesterov momentum` | `contrastive loss to alleviate the ` | `512 × 512 pixel` | [[P21 chunks#^P21_c030\|c030]] |
| [[P25 Chen 2021\|P25]] | `learning rate is initially set to ` |  | `200 epochs` | `SGD) with momentum to optimize the` | `crossentropy loss to optimize the ` |  | [[P25 chunks#^P25_c029\|c029]] |
| [[P26 Bandara 2022\|P26]] | `learning rate is initially set to ` | `batch size of 16 to train the mode` | `200 epochs` | `AdamW optimizer with weight decay ` |  |  | [[P26 chunks#^P26_c014\|c014]] |
| [[P27 Zheng 2021\|P27]] | `learning rate was set to 0.03 and ` |  |  | `SGD as the optimizer on single Tit` | `binary cross-entropy loss Lbinary ` | `1024×1024 pixel` | [[P27 chunks#^P27_c021\|c021]] |
| [[P28 Chen 2024\|P28]] | `learning rate of 1e−4 and a weight` | `batch size is set to 16` |  | `AdamW optimizer [67] with a learni` | `focal loss [63], deep supervision ` | `1024 × 1024 pixel` | [[P28 chunks#^P28_c040\|c040]] |
| [[P29 Zheng 2024\|P29]] |  |  |  |  | `BCE loss with a label smoothing of` |  | [[P29 chunks#^P29_c030\|c030]] |
| [[P30 Yongshuo 2025\|P30]] |  | `batch size of 1 and trained for 30` | `300 epochs` |  | `cross-entropy loss for supervised ` |  | [[P30 chunks#^P30_c014\|c014]] |
| [[P31 Huang 2025\|P31]] | `learning rate of 0.1` | `batch size is set to 8, with an in` |  | `SGD) optimizer is utilized with a ` | `dice loss (Milletari et al` |  | [[P31 chunks#^P31_c018\|c018]] |
| [[P32 Szwarcman 2024\|P32]] | `learning rate of 5e-4 and linear w` | `batch size (i` | `400 epochs` | `Adam optimizer with a learning rat` | `cross-entropy and the models ran f` | `64 × 64 patch` | [[P32 chunks#^P32_c022\|c022]] |
| [[P33 Bou 2026\|P33]] | `learning rate of 1e-4` |  | `100 epochs` | `AdamW optimizer [44] with a 1e-2 w` | `focal losses` | `512 × 512 FLAIR image patch` | [[P33 chunks#^P33_c022\|c022]] |
| [[P34 Shen 2026\|P34]] | `learning rate, SSCLoss yields a 10` | `batch size is set to 8 and the wei` |  | `SGD) optimizer with momentum` |  | `512 × 512 size and is annotated at` | [[P34 chunks#^P34_c009\|c009]] |
| [[P35 Su 2026\|P35]] | `learning rate of 1 × 10−3, a batch` | `batch size of 4, and 20 epochs` | `20 epochs` |  | `binary cross-entropy loss between ` | `613 × 19,990 pixel` | [[P35 chunks#^P35_c026\|c026]] |
| [[P36 Shu 2025\|P36]] | `learning rate of 0.0001 and a weig` | `batch size, N is the sequence leng` |  | `AdamW is employed, with a learning` | `cross-entropy loss to mitigate the` | `256 × 256 patch` | [[P36 chunks#^P36_c038\|c038]] |
| [[P38 Buslaev 2018\|P38]] | `learning rate 1e-4 and decay 1e-4 ` | `batch size of 8 images` |  | `Adam optimizer with learning rate ` | `binary cross entropy, while for a ` | `1024x1024 pixel` | [[P38 chunks#^P38_c010\|c010]] |
| [[P39 Bernhard 2023\|P39]] |  |  |  |  | `contrastive loss to guide the lear` |  | [[P39 chunks#^P39_c002\|c002]] |
| [[P40 Lee 2026\|P40]] | `learning rate to 0.00006 to ensure` | `batch size was configured to 6, co` |  | `AdamW optimizer for weight updates` | `contrastive loss (Lcon)` | `512 × 512 pixel tile` | [[P40 chunks#^P40_c030\|c030]] |
| [[P45 Brown 2022\|P45]] |  |  |  |  |  | `510 × 510 pixel` | [[P45 chunks#^P45_c006\|c006]] |
| [[P49 Lei 2026\|P49]] |  |  |  |  | `contrastive loss function based on` |  | [[P49 chunks#^P49_c056\|c056]] |
| [[P52 Georganos 2018\|P52]] | `learning rate, tree depth and subs` |  |  |  |  |  | [[P52 chunks#^P52_c011\|c011]] |
| [[P53 Tianqi 2016\|P53]] | `learning rate in tochastic optimiz` |  |  |  |  |  | [[P53 chunks#^P53_c012\|c012]] |
| [[P56 Osco 2023\|P56]] | `learning rate is scheduled using t` |  | `1000 epochs` |  |  |  | [[P56 chunks#^P56_c032\|c032]] |
| [[P63 Dabaja 2026\|P63]] |  |  |  |  |  | `600 × 600 pixel` | [[P63 chunks#^P63_c015\|c015]] |
| [[P64 Siméoni 2025\|P64]] | `learning rate, weight decay, and t` | `batch size of 131K` | `22 epochs` | `AdamW (Loshchilov and Hutter, 2017` | `contrastive losses and the joint-t` | `1024 × 1024 pixel` | [[P64 chunks#^P64_c033\|c033]] |
| [[P65 Faulkenberry 2026\|P65]] |  | `batch size of 4 for 45,000 iterati` |  |  |  | `512 × 512 and perform sliding wind` | [[P65 chunks#^P65_c020\|c020]] |
| [[P67 Xiong 2024\|P67]] | `learning rates and batch sizes tai` | `batch size from the notation of te` | `50 epochs` | `AdamW optimizer, batch size 64, an` | `cross-entropy loss for most datase` |  | [[P67 chunks#^P67_c030\|c030]] |
| [[P70 Simões 2021\|P70]] |  |  |  |  |  | `204 × 7324 pixel` | [[P70 chunks#^P70_c034\|c034]] |
| [[P76 Kerdreux 2025\|P76]] | `learning rate` | `batch size of 256, an AdamW optimi` | `200 epochs` | `AdamW optimizer, a cosine schedule` | `focal loss or self-paced reweighti` |  | [[P76 chunks#^P76_c021\|c021]] |
| [[P79 Reed 2022\|P79]] | `learning rate of 5 × 10−3, a weigh` | `batch size of 256 across 2 GPUs` | `800 epochs` |  |  | `100x100 pixel` | [[P79 chunks#^P79_c026\|c026]] |
| [[P90 Karwowska 2022\|P90]] |  |  |  |  |  | `1280 × 720 pixel` | [[P90 chunks#^P90_c046\|c046]] |
| [[P100 Crato 2025\|P100]] |  | `batch size, Epochs), the number of` | `50 epochs` |  |  | `41x41 pixel` | [[P100 chunks#^P100_c020\|c020]] |
| [[P102 Masolele 2024\|P102]] | `learning rate of 10−4 ` | `batch size of 64, using Adam optim` | `200 epochs` | `Adam optimization with a learning ` | `focal loss has shown to perform we` |  | [[P102 chunks#^P102_c026\|c026]] |
| [[P103 Glazer 2025\|P103]] | `learning rate of 1.4e−3 and a batc` | `batch size of 64` |  | `AdamW” optimizer with a tuned lear` |  | `4096 x 4096 pixel` | [[P103 chunks#^P103_c019\|c019]] |
| [[P105 He 2022\|P105]] | `learning rate 2 × 10−3, β0 = 0, β1` |  |  | `Adam optimizer with learning rate ` |  | `1024 × 1024 pixel` | [[P105 chunks#^P105_c011\|c011]] |
| [[P106 Rahul 2023\|P106]] |  |  |  |  |  |  | [[P106 chunks#^P106_c008\|c008]] |
| [[P110 Alshehri 2024\|P110]] | `learning rates 0.01 - 0.0001 Loss ` |  | `200 epochs` | `SGD, Adam, AdamW learning rates 0` | `cross-entropy loss with AdamW opti` | `256×256 pixel` | [[P110 chunks#^P110_c016\|c016]] |
| [[P112 Andrade 2020\|P112]] | `learning rate of 0.001 and weight ` | `batch size was set to 32` | `10 epochs` | `Adam optimizer, with the learning ` | `focal loss function (Lin et al` | `64×64 pixel` | [[P112 chunks#^P112_c023\|c023]] |
| [[P113 Jelas 2024\|P113]] | `learning rate of 0.003, a batch si` | `batch size of 16, and the Adaptive` | `90 epochs` | `Adam) optimizer` | `binary crossentropy as a loss func` |  | [[P113 chunks#^P113_c104\|c104]] |
| [[P115 McCallum 2023\|P115]] | `learning rate of 1 × 10−3, a batch` | `batch size of 32, and an L2 regula` | `30 epochs` |  | `cross-entropy loss J as follows: J` |  | [[P115 chunks#^P115_c017\|c017]] |
| [[P118 Reiche 2024\|P118]] |  |  |  |  |  | `20 × 22 m (10 m pixel` | [[P118 chunks#^P118_c023\|c023]] |
| [[P122 Cortinhas 2024\|P122]] |  |  |  |  |  | `256 × 256 pixel` | [[P122 chunks#^P122_c039\|c039]] |
| [[P126 Shafique 2022\|P126]] |  |  |  |  | `cross-entropy loss function, which` |  | [[P126 chunks#^P126_c062\|c062]] |
| [[P127 Miller 2024\|P127]] |  |  |  |  | `contrastive loss (CSCL) was especi` |  | [[P127 chunks#^P127_c105\|c105]] |
| [[P130 Shen 2021\|P130]] |  |  |  |  | `contrastive loss, which is designe` | `1024 × 1024 pixel` | [[P130 chunks#^P130_c014\|c014]] |
| [[P132 Zhou 2025\|P132]] | `learning rate of 0.0005, a cosine ` | `batch size of 16, followed by 4000` | `12,000 epochs` | `AdamW optimizer [61] with an initi` | `binary cross-entropy and Dice loss` | `1024 × 1024 pixel` | [[P132 chunks#^P132_c033\|c033]] |
| [[P133 Ding 2024\|P133]] | `learning rate to 0.1 and update it` |  | `50 epochs` |  |  | `1024×1024 pixel` | [[P133 chunks#^P133_c019\|c019]] |
| [[P137 Li 2024\|P137]] | `learning rate is set to 0.0001, an` | `batch size is set to 8` | `50 epochs` | `AdamW optimizer` | `cross-entropy loss for BiT and Cha` | `507 × 15,354 pixel` | [[P137 chunks#^P137_c029\|c029]] |
| [[P138 Zhang 2025\|P138]] | `learning rate at 0.1 and updated i` |  | `100 epochs` | `SGD) with Nesterov momentum` | `cross-entropy loss between the sem` | `512×512 pixel` | [[P138 chunks#^P138_c028\|c028]] |
| [[P139 Benidir 2025\|P139]] | `learning rate of 3e-4 with exponen` | `batch size of 32)` |  |  | `Focal losses [31]: minimizing high` |  | [[P139 chunks#^P139_c025\|c025]] |
| [[P141 Guo 2025\|P141]] | `learning rate of 0.1` | `batch size is 4 and the model is t` | `50 epochs` | `SGD optimizer with an initial lear` |  | `512 × 512 pixel` | [[P141 chunks#^P141_c022\|c022]] |
| [[P145 Zhang 2025\|P145]] | `learning rate of 5×10−5` | `batch size of 1 and a gradient acc` | `10 epochs` | `AdamW [36] optimizer with a base l` | `BCELBCE + λDiceLDice + λSSLSS + λS` | `1024 × 1024 patch` | [[P145 chunks#^P145_c023\|c023]] |
| [[P146 Papadomanolaki 2019\|P146]] | `learning rate values were equal to` | `batch size and learning rate value` |  | `Adam while batch size and learning` |  |  | [[P146 chunks#^P146_c011\|c011]] |
| [[P148 Chen 2021\|P148]] |  |  |  |  | `contrastive loss and an implicit c` |  | [[P148 chunks#^P148_c001\|c001]] |
| [[P150 Wu 2023\|P150]] | `learning rate of discriminator is ` | `batch size is 10` |  | `Adam optimizer and warmup strategy` | `BCE loss to the pixel-level refere` |  | [[P150 chunks#^P150_c018\|c018]] |
| [[P151 Lu 2025\|P151]] |  |  |  |  |  |  | [[P151 chunks#^P151_c024\|c024]] |
| [[P154 Ramos-Pollán 2024\|P154]] |  |  |  |  |  | `512 × 512 pixel` | [[P154 chunks#^P154_c009\|c009]] |
| [[P165 Wang 2025\|P165]] |  |  |  |  |  |  | [[P165 chunks#^P165_c021\|c021]] |
| [[P175 Šanca 2023\|P175]] |  | `batch size, yi is the ground truth` |  | `Adam optimizer with Binary Cross E` |  |  | [[P175 chunks#^P175_c017\|c017]] |
| [[P179 Robinson 2026\|P179]] | `learning rate of 0.0001, and achie` |  | `10 epochs` | `AdamW optimizer with a learning ra` |  |  | [[P179 chunks#^P179_c010\|c010]] |
| [[P184 Ramadan 2022\|P184]] | `learning rate, and the neighborhoo` |  |  |  |  |  | [[P184 chunks#^P184_c020\|c020]] |
