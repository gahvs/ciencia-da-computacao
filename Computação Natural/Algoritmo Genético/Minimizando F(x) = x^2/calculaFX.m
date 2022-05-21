function FX = calculaFX(POP,problema)
    switch problema
        case 1
            FX = POP .^ 2;
        case 2
            FX = rastrigin(POP);
        otherwise
            fprintf('PROBLEMA NÃO ENCONTRADO\n');
            return;
    end
    
end