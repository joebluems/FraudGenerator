### run these commands in R to generate a simple logistic model to show coefficients are significant ###
training <-read.csv("/Users/jblue/BLOGS/FRAUD/model.csv")
colnames(training) = c("account","target","dslt")
glm.out = glm(target ~ dslt, family=binomial(logit), data=training)
summary(glm.out)

<--------- model output ----------->
Call:
glm(formula = target ~ dslt, family = binomial(logit), data = training)

Deviance Residuals: 
    Min       1Q   Median       3Q      Max  
-0.4949  -0.3691  -0.2826  -0.2335   2.9004  

Coefficients:
            Estimate Std. Error z value Pr(>|z|)    
(Intercept) -2.03817    0.02442  -83.45   <2e-16 ***
dslt        -0.55918    0.01458  -38.35   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 40079  on 99998  degrees of freedom
Residual deviance: 38560  on 99997  degrees of freedom
AIC: 38564

Number of Fisher Scoring iterations: 6
