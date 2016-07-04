import matplotlib.pyplot as plt

class LetMeVisualizeThat(object):
    def __init__(self, dictionary_dataset_to_plot):
        self.data = dictionary_dataset_to_plot

    def plot_bar_chart_words(self):
        # return the keys of the dictionary after sorting it by its values in a desc order
        # pick top 6 only
        x = sorted(self.data, key=self.data.__getitem__, reverse=True)[:6]
        y = [self.data[key] for key in x]

        # create an instance of an figure object
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

        # Define spectral types
        spectral_id = [1, 2, 3, 4, 5, 6]
        spectral_types = x

        # Plot the data
        width = 1/1.5
        ax.bar(spectral_id, y, width, align = 'center', color = 'red')
        ax.set_xlim(0., 7)
        ax.set_ylim(0., max(y) + 1)

        # Set the custom ticks on the x-axis
        ax.set_xticks(spectral_id)
        ax.set_xticklabels(spectral_types)
        ax.set_title("Bad things people pay for via Venmo (Words)", fontsize='large')
        ax.set_xlabel("Substances related words")
        ax.set_ylabel("Frequency")
        fig.show()

    def plot_bar_chart_emojis(self):
        # return the keys of the dictionary after sorting it by its values in a desc order
        # pick top 6 only
        x = sorted(self.data, key=self.data.__getitem__, reverse=True)[:6]
        y = [self.data[key] for key in x]

        # create an instance of an figure object
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

        # Define spectral types
        spectral_id = [1, 2, 3, 4, 5, 6]
        spectral_types = x

        # Plot the data
        width = 1/1.5
        ax.bar(spectral_id, y, width, align = 'center', color = 'red')
        ax.set_xlim(0., 7)
        ax.set_ylim(0., max(y) + 1)

        # Set the custom ticks on the x-axis
        ax.set_xticks(spectral_id)
        ax.set_xticklabels(spectral_types)
        ax.set_title("Bad things people pay for via Venmo (Emojis)", fontsize='large')
        ax.set_xlabel("Substances related emojis")
        ax.set_ylabel("Frequency")
        plt.show()
