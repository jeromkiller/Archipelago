from .. import SohWorld
from ..Enums import Regions
from ..Items import Items
from .bases import SohTestBase

class TestDekuTreeUpperBasement(SohTestBase):
    options = {"starting_age": 0, "closed_forest": 2, "door_of_time": 0}
    world: SohWorld

    def test_child_without_slingshot_cannot_access_upper_basement_normally(self):
        self.collect_by_name(Items.KOKIRI_SWORD)
        self.assertTrue(self.can_reach_region(Regions.DEKU_TREE_BASEMENT_LOWER), f"The basement should be accessible.")
        self.assertFalse(self.can_reach_region(Regions.DEKU_TREE_BASEMENT_UPPER),
                         f"An unskilled child cannot get to the top of the basement.")

    def test_child_without_slingshot_with_trick_can_access_upper_basement(self):
        self.enable_glitched_item()
        self.collect_by_name(Items.KOKIRI_SWORD)
        self.assertTrue(self.can_reach_region(Regions.DEKU_TREE_BASEMENT_UPPER),
                        f"A skilled child can go from lower basement to upper basement without pushing the block.")
