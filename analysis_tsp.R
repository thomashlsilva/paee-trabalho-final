# Instala pacotes necessários, se ainda não estiverem instalados
if (!require(ggplot2)) install.packages("ggplot2")
if (!require(reshape2)) install.packages("reshape2")

library(ggplot2)
library(reshape2)

# Escolha do cenário
scenario <- "si1032" # "pa561", "si535" ou "si1032"

# Leitura do CSV
data <- read.csv(paste0(scenario, ".csv"))

# Converter para formato longo para plotagem
data_long <- melt(data)

# Plotagem da densidade
p <- ggplot(data_long, aes(x=value, colour=variable)) +
  geom_density() +
  labs(title=paste("Densidade de distribuição -", scenario),
       x="Custo",
       y="Densidade") +
  theme_minimal()

print(p)

# Salvar o gráfico
ggsave(paste0("densidade_", scenario, ".png"), plot=p)

# Teste de normalidade de Shapiro-Wilk
cat("\nTeste de normalidade para SA:\n")
print(shapiro.test(data$SA))

cat("\nTeste de normalidade para GRASP:\n")
print(shapiro.test(data$GRASP))
