library(foreign)
library(tree)

x <- read.csv(file = "extracted_data.csv", header = TRUE, sep = ",")

# 450 top players
tree_1 <- tree(p_wage ~ . , data = x)
summary(tree_1)
plot(tree_1)
text(tree_1, pretty = 0)

# cross validation to select the number of nodes

cv_tree <- cv.tree(tree_1)

# Illustrate
plot(cv_tree$size, cv_tree$dev, type = "b")

# prune the tree with the selected number
prune_tree <- prune.tree(tree_1, best = 7)
plot(prune_tree)
text(prune_tree , pretty = 0)


#####
##### 446 top players with the supper top four player removed

x <- x[x$p_wage < 406700,]

tree_2 <- tree(p_wage ~ . , data = x)
summary(tree_2)
plot(tree_2)
text(tree_2, pretty = 0)

# cross validation to select the number of nodes

cv_tree <- cv.tree(tree_2)

# Illustrate
plot(cv_tree$size, cv_tree$dev, type = "b")

# prune the tree with the selected number
prune_tree <- prune.tree(tree_2, best = 5)
plot(prune_tree)
text(prune_tree , pretty = 0)



