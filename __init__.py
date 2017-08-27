import bpy

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

def unregister():
    bpy.utils.unregister_module(__name__)
