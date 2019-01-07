def create_model(opt):
    model = None
    print(opt.model)
    if opt.model == 'shiftnet':
        assert (opt.dataset_mode == 'aligned' or opt.dataset_mode == 'aligned_resized')
        from models.shift_net.shiftnet_model import ShiftNetModel
        model = ShiftNetModel()

    elif opt.model == 'res_shiftnet':
        assert (opt.dataset_mode == 'aligned' or opt.dataset_mode == 'aligned_resized')
        from models.res_shift_net.shiftnet_model import ResShiftNetModel
        model = ResShiftNetModel()

    elif opt.model == 'soft_shiftnet':
        assert (opt.dataset_mode == 'aligned' or opt.dataset_mode == 'aligned_resized')
        from models.soft_shift_net.soft_shiftnet_model import SoftShiftNetModel
        model = SoftShiftNetModel()

    elif opt.model == 'patch_soft_shiftnet':
        assert (opt.dataset_mode == 'aligned' or opt.dataset_mode == 'aligned_resized')
        from models.patch_soft_shift.patch_soft_shiftnet_model import PatchSoftShiftNetModel
        model = PatchSoftShiftNetModel()

    elif opt.model == 'res_patch_soft_shiftnet':
        assert (opt.dataset_mode == 'aligned' or opt.dataset_mode == 'aligned_resized')
        from models.res_patch_soft_shift.res_patch_soft_shiftnet_model import ResPatchSoftShiftNetModel
        model = ResPatchSoftShiftNetModel()

    elif opt.model == 'bilinear_shiftnet':
        assert (opt.dataset_mode == 'aligned' or opt.dataset_mode == 'aligned_resized')
        from models.bilinear_shift_net.shiftnet_model import BilinearShiftNet
        model = BilinearShiftNet()

    elif opt.model == 'test':
        assert(opt.dataset_mode == 'single')
        from .test_model import TestModel
        model = TestModel()
    else:
        raise ValueError("Model [%s] not recognized." % opt.model)
    model.initialize(opt)
    print("model [%s] was created" % (model.name()))
    return model
