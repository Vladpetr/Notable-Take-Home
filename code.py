from word2number import w2n


class NoteTransformation:
    def __init__(self, note):
        if not note:
            self.note = input("Unfortunately we could not recognize a note. "
                              "Could you please enter it below?")

        self.note = note
        self.cur_number = None

    def transform(self):
        transformed_note = ""
        words = self.note.split(" ")
        idx = 0
        # iterate through every word in the input
        while idx < len(words):
            # check if the word is "number"
            if words[idx].lower() != "number":
                transformed_note += (words[idx] + " ")

            else:
                if idx >= len(words) - 1:
                    transformed_note += (words[idx])
                # check if the next word after "number" is "next" and
                # if the numbered list has already been started
                elif (self.cur_number and words[idx + 1].lower() != "next") or \
                        (not self.cur_number and words[idx + 1].lower() == "next"):
                    transformed_note += (words[idx] + " ")

                else:
                    # strip the trailing whitespace on the right
                    transformed_note = transformed_note.rstrip()
                    idx += 1

                    if words[idx].lower() != "next":
                        # convert a number in text format to integer
                        number = w2n.word_to_num(words[idx])

                        # check if the first number in the list is 1
                        # if not, make blank list points until the identified number is reached
                        if not self.cur_number:
                            if number == 1:
                                pass
                            elif 1 < number <= 9:
                                for i in range(1, number):
                                    transformed_note += "\n"
                                    transformed_note += (str(i) + ". ")
                            else:
                                raise ValueError("The starting number should be from one to nine. "
                                                 "Please make changes to the first entry in the numbered list.")

                        # keep track of the current list number
                        self.cur_number = number
                    else:
                        self.cur_number += 1
                        number = self.cur_number

                    transformed_note += "\n"
                    transformed_note += (str(number) + ". ")
                    # capitalize the first letter of the next word
                    if words[idx + 1][0] != words[idx + 1][0].upper():
                        words[idx + 1] = words[idx + 1].capitalize()

            idx += 1

        transformed_note = transformed_note.rstrip()
        return transformed_note


notable_example = "Patient presents today with several issues. Number one BMI has increased by 10% " \
                  "since their last visit number next patient reports experiencing dizziness several times " \
                  "in the last two weeks. Number next patient has a persistent cough that hasn’t " \
                  "improved for last 4 weeks Number next patient is taking drug number five several " \
                  "times a week"
test1 = NoteTransformation(notable_example)
print(test1.transform())
