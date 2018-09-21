#! /vol/ek/nalam82/R/R-3.3.2/bin/Rscript

system("printScoreFile_byHeader.pl rescore.sc I_sc reweighted_sc rmsBB description | sed 1d |  sort -nk 3 | head -5000 | awk '{print \"Sampling\",$2,$3,$4,$5}' >mod_score.sc", wait=FALSE)
system("for i in `sed 1d cluster_list_I_sc_sorted | awk '{print $1}'`;do grep $i mod_score.sc;done | awk '{print \"I_sc_clusters\",$2,$3,$4,$5}' >>mod_score.sc", wait=FALSE)
system("for i in `sed 1d cluster_list_reweighted_sc_sorted | awk '{print $1}'`;do grep $i mod_score.sc;done | awk '{print \"reweighted_sc_clusters\",$2,$3,$4,$5}' >>mod_score.sc", wait=FALSE)

library(ggplot2)
data = read.table("mod_score.sc")
data_I_sc <- data[ which( data$V1 =="Sampling" | data$V1 == "I_sc_clusters") , ]
data_rewighted_sc <- data[ which( data$V1 =="Sampling" | data$V1 == "reweighted_sc_clusters") , ]


tiff("sampling_I_sc.tiff", width=1.85, height=1.8, units='in', res=300)
ggplot(data_I_sc,aes(x=V4,y=V2,color=V1)) + geom_point(size=1.5,shape=20, stroke=0.15) + theme(panel.background = element_rect(fill = "white"), axis.line.x = element_line(color="black", size = 0.05),axis.line.y = element_line(color="black", size = 0.025), legend.position='bottom') + theme(text=element_text(size=10, family="Arial")) + scale_x_continuous(breaks = seq(0,50.0,5.0), limits = c(0,35)) + theme(axis.ticks.length = unit(.05, "cm")) + xlab("rmsBB") + ylab("I_sc") + theme(plot.title = element_text(hjust = 0.5)) + scale_fill_manual(values=c("#0072B2","#999999")) + scale_color_manual(values=c("#0072B2","#999999")) + theme(legend.position="none")
dev.off()

tiff("sampling_reweighted_sc.tiff", width=1.85, height=1.8, units='in', res=300)
ggplot(data_rewighted_sc,aes(x=V4,y=V3,color=V1)) + geom_point(size=1.5,shape=20, stroke=0.15) + theme(panel.background = element_rect(fill = "white"), axis.line.x = element_line(color="black", size = 0.05),axis.line.y = element_line(color="black", size = 0.025), legend.position='bottom') + theme(text=element_text(size=10, family="Arial")) + scale_x_continuous(breaks = seq(0,100.0,5.0), limits = c(0,35)) + theme(axis.ticks.length = unit(.05, "cm")) + xlab("rmsBB") + ylab("reweighted_sc") + theme(plot.title = element_text(hjust = 0.5)) + scale_fill_manual(values=c("#E69F00","#999999")) + scale_color_manual(values=c("#E69F00","#999999")) + theme(legend.position="none")
dev.off()
