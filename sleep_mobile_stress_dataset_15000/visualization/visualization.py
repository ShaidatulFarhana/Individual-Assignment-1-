import matplotlib.pyplot as plt
import seaborn as sns

def plot_analysis(df):
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Sleep and Stress Data Analysis', fontsize=20)

    # Histogram
    sns.histplot(df['sleep_quality_score'], bins=20, kde=True, ax=axes[0, 0], color='skyblue')

    # Bar Chart
    avg_screen_time = df.groupby('occupation')['daily_screen_time_hours'].mean().sort_values()
    sns.barplot(x=avg_screen_time.values, y=avg_screen_time.index, ax=axes[0, 1], hue=avg_screen_time.index, palette='magma')

    # Box Plot
    sns.boxplot(data=df, x='gender', y='stress_level', ax=axes[1, 0], hue='gender', palette='Set2')

    # Line Plot
    sns.lineplot(data=df, x='caffeine_intake_cups', y='mental_fatigue_score', ax=axes[1, 1], color='brown', marker='o')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
