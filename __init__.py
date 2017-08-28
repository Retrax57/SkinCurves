'''
Created by Retrax

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import bpy
from bpy.types import (
        AddonPreferences,
        Operator,
        Panel,
        Menu,
        )

bl_info = {
    "name": "Skin Curves",
    "description": "Skin Modifier based curve generation",
    "author": "Retrax",
    "version": (0, 0, 1),
    "blender": (2, 78, 0),
    "location": "View3D",
    "warning": "This is an unstable version",
    "wiki_url": "",
    "category": "Curves" }

#Rename Update------------------------------------------------------------------        
def update_panel(self, context):
    try:
        bpy.utils.unregister_class(SkinCurves)
    except:
      pass
    SkinCurves.bl_category = context.user_preferences.addons[__name__].preferences.category
    bpy.utils.register_class(SkinCurves) 

#Preferences---------------------------------------------------------------------
class RenamePreferences(AddonPreferences): 
    bl_idname = __name__ 
    category = bpy.props.StringProperty(
        name="Category", 
        description="Choose a name for the Category of the panel", 
        default="SkinCurves", 
        update=update_panel) 
    def draw(self, context): 
        layout = self.layout
        col = layout.column(align=True)
        row = col.row(align=True)
        row.label(text="Choose a name for the Category of the panel:")
        row.prop(self, "category", text="") 
        row = col.row(align=True)
        row.label("")
        row = col.row(align=True)
        row.label("")
        row = col.row(align=True)
        row.label("", icon='COLOR')
        row.label("If you are seeing this then SkinCurves has been sucessfully installed, whew ! Enjoy !")
        row = col.row(align=True)
        row.label("", icon='COLOR')
        row.label("You can message me on facebook or just send me an email if you have any questions or want to report a bug:")
        row = col.row(align=True)
        row.label("")
        row = col.row(align=True)
        row.scale_x = 4.0
        row.scale_y = 4.0
        row.operator("wm.url_open", text="My Facebook Account").url = "https://www.facebook.com/Retrax57"
        row.operator("wm.url_open", text="My Email Address").url = "https://www.retrax57@gmail.com"
        row.operator("wm.url_open", text="My Github page").url = "https://www.github.com/Retrax57"
        row.operator("wm.url_open", text="Youtube Channel").url = "https://www.youtube.com/channel/UCpwCLBFgMorDxvxSoi-yniQ"


class addskincurve(bpy.types.Operator):
    bl_idname = "add.skincurve"
    bl_label = "Addskincurve"
    bl_options = {"REGISTER"}

    def execute(self, context):
        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.context.object.modifiers.new("SkinCurve", "SKIN")
        bpy.context.object.modifiers["SkinCurve"].use_smooth_shade = True

        bpy.context.object.modifiers.new("Smoother", "SUBSURF")
        bpy.context.object.modifiers["Smoother"].levels = 3
        bpy.context.object.modifiers["Smoother"].render_levels = 3
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 1), "constraint_axis":(False, False, True), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.transform.translate(value=(0, 0, -0.5), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.transform.resize(value=(2, 2, 2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.context.space_data.use_occlude_geometry = False


        return {"FINISHED"}
    
class SkinCurves(bpy.types.Panel):
    bl_idname = "skin_curves"
    bl_label = "Skin Curves"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "SkinCurves"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        row = col.row(align=True)
        row.scale_x=1.0
        row.scale_y=3.0
        row.operator("add.skincurve", text='Add SkinCurve')
        skin = context.object.modifiers["SkinCurve"]      
        smo = context.object.modifiers["Smoother"]        
        if bpy.context.object and bpy.context.object.modifiers["SkinCurve"] and bpy.context.object.modifiers["Smoother"] is not None:
            row = col.row(align=True)
            row.scale_x=5.0
            row.scale_y=1.5
            row.alignment = 'CENTER'
            row.prop(skin, "use_smooth_shade", text="", icon='SOLID')  
            row.prop(smo, "show_only_control_edges", text="", icon='MESH_ICOSPHERE')  
            row = col.row(align=True)
            row.prop(smo, "levels", text="Sub View")
            row = col.row(align=True)
            row.prop(smo, "render_levels", text="Sub Render")
            row = col.row(align=True)
            row.alignment = 'CENTER'
            row.label("CTRL+A To scale points")
            
                
def register():
    bpy.utils.register_module(__name__)
    update_panel(None, bpy.context) 

def unregister():
    bpy.utils.unregister_module(__name__)
