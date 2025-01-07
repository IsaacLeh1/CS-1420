# yondu.py

# Get the total number of pirates and units from the user
num_pirates = int(input("Enter the number of pirates including Yondu and Peter: "))
total_units = int(input("Enter the total number of units ther pirates boarded the ship with: "))

# Calculation of unit distribution of 3 units per pirate minus yondu and peter (the 2)
total_units = total_units - (num_pirates-2) * 3
crews_share = 3

# Yondu's share 13% of the total units
yondus_share = round(total_units*0.13, 2)
total_units = total_units - yondus_share

# Peter's share (11% after yondus share)
peters_share = round(total_units*0.11, 2)
total_units = total_units - peters_share

# Calculate the share for the rest of the crew after Yondu and Peter's cut
crews_share_cut = round(total_units / num_pirates, 2)

#Adding the cuts to Peter, Yondu and the crew
peters_share = peters_share + crews_share_cut
yondus_share = yondus_share + crews_share_cut
crews_share = crews_share + crews_share_cut

print("Yondu's share: ", yondus_share)
print("Peter's share: ", peters_share)
print("Crew's share: ", crews_share)