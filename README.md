# djenerator-GAN

A take on using Ian Goodfellow et al's Generative Adversarial Network (GAN) model to generate music samples with a style of Djent (this term usually describes the sound of chugging on the guitar within breakdowns or verses, alongside with syncopated rhythms on both drums and guitars).

## Purpose

The reason I wanted to work on this project is that I wanted to combine two things I love, progressive metal music and programming, in order to experiment with data generation, specifically music. I have seen many projects that have generation as their based, though I couldn't really find something that I was interested in (pure computer-generated music), as most of them used context in order to generate (PixelRNN, WaveNet and whatnot) and/or used midi files instead of raw .wav files (GANSynth).

Of course, there might be projects out there that achieved what I am merely attempting to achieve with my project, though I wanted to make something that seems interesting, as in: how would computer-generated progressive metal sound like? How would it manage to find patterns such as rhythm syncopated guitars and odd-time signature combos in order to generate breakdowns, etc...

This project is both a diary, in which I store the process and progress of this experiment, and a tool that I intend to use as an API to a possible web app made for fun.

After finishing with experimentation, the next step would probably be some sort of user interface with a web audio player hooked to this API.

Thus, I will keep this README both for information (for anyone interested) and for myself, such that I can keep track of things and maybe have something to look back upon in the future.

## Current state of the project + Ideas to implement

Here I'll put some checkboxes to keep track of what ideas I have implemented. Once the experiment becomes stable, I'll update this description.

- [x] The current architecture I used to create this model is a simple at base, it consisting in some dense layers for both the discriminator and the generator, with their respective activation functions and regularization layers (see "djenerator.ipynb").

- [ ] Something that definitely <b>has</b> to be done is more data gathering. For the purpose of the experiment, I used 8 .wav files, the content of which I have divided in 50 vectors of 30 seconds of content with values between -1 and 1 (sine wave).

## Encountered problems & possible solutions

During training (specifically, at around 45000 epochs) I noticed that the loss of the discriminator with respect to the real data and the fake data was converging and the generator's loss (discriminator's inverse loss with respect to the fake data) was diverging. This is known as the <b>vanishing gradient</b> problem. I hoped that I wouldn't be a victim of such problem, but I was wrong.

Some possible solutions (I will tick the ones that I have / I am currently trying) are:

- [x] Adding noise to the real data before feeding it to the discriminator:

    ```py
    real += 0.2 * torch.randn(noise_size)
    ```

- [x] Smoothing out the label vectors of ones as being 0.9 instead of 1

- [x] Replacing the Adam optimizer with RMSprop(lr = 0.001, alpha = 0.7, epsilon = 0.0001)

- [ ] Implementing a Kullback-Leibler Divergence loss as an alternative to the Binary Cross-Entropy loss.

- [ ] Converting the current GAN architecture into a WGAN architecture, using the Wasserstein loss as the main way for calculating the error.

## Samples

The samples will be located in the "djenerated_samples_wav" folder [here](https://drive.google.com/drive/folders/1-YXiEGL8uS-O2A9DcjIQK-qQuDCIK6zc?usp=sharing), though, before fully succeeding with this experiment, I advise you to either listen to them with a low volume or be prepared to listen to them at 100% volume, as there is <b>a lot</b> of generated white noise, which is quite unpleasent. Currently, the sample at the 39500th epoch is the latest one (before applying the possible solutions to the vanishing gradient problem). If you listen closely you can hear some drums and some distorted guitars-like sounds in the background (unfortunately, white noise is predominant).

With the applied changes, we can see improvements as soon as the 2000th epoch (still with white noise, but getting closer). It seems to be able to copy some features perfectly from the dataset (an example is Jason Richardson solo from the song Tonga, in around 7 / 20 samples it repeats it, so it really caught on to that solo's pattern), which means the model is overfitting. This is good news as all we need to do from now on to avoid overfitting and achieve generalization is to regularize the layers and gather more data.
